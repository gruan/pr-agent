"""
Runs a PR command writing title and description via GPT-4o
"""

import os
import subprocess
import sys

import openai


def main():
    """
    Main function to generate a prompt for a GitHub PR command.
    """

    # Check os.environ for PR_AGENT_OPENAI_API_KEY
    if "PR_AGENT_OPENAI_API_KEY" not in os.environ:
        print("Error: PR_AGENT_OPENAI_API_KEY not found in environment variables")
        sys.exit(1)

    # Get the current branch name
    current_branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    # Pipe bash `git show` to python variable `commit_changes`
    commit_changes = subprocess.run(
        ["git", "show"], capture_output=True, text=True, check=True
    ).stdout

    # Generate prompt
    prompt = f"""
    Write a gh pr command with a --title and --body for the following commit changes.
    Use the --web feature to allow users to pick the correct repo and branch.

    For the body use markdown formatting and create a section for each of the following:
    - Goals
    - Key Changes
    - Tests

    Current branch:
    ```
    {current_branch}
    ```

    Commit changes:
    ```
    {commit_changes}
    ```

    Output the command only. Use markdown formatting.
    """
    # print(prompt)

    # Call OpenAI API using environment variables
    client = openai.OpenAI(api_key=os.getenv("PR_AGENT_OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

    command = response.choices[0].message.content
    assert command is not None

    # Strip blank lines
    command = command.strip()

    # Remove the ``` markdown block
    command = command.replace("```bash\n", "")
    command = command.replace("```", "")

    # Remove the ` backticks since they cause issues with bash
    command = command.replace("`", "")

    # Ensure it starts with `gh pr create`
    if not command.startswith("gh pr create"):
        print("Error: Command does not start with `gh pr create`")
        sys.exit(1)

    # Directly run the bash command.
    subprocess.run(command, shell=True, check=True)


# Run if __main__
if __name__ == "__main__":
    main()
