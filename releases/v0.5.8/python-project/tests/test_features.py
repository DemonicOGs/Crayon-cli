from crayon_cli.policy import evaluate_command

def test_read_only_blocks_write_command():
    result = evaluate_command("rm file.txt", "read-only")
    assert result["allowed"] is False

def test_destructive_command_requires_review():
    result = evaluate_command("rm -rf ./build", "workspace-write")
    assert result["decision"] == "review"

def test_unrestricted_is_explicit():
    result = evaluate_command("rm -rf ./build", "unrestricted")
    assert result["allowed"] is True

def test_read_command_allowed():
    result = evaluate_command("git status", "workspace-write")
    assert result["allowed"] is True
