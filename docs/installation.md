# Installation and updates / 安装与更新

Requires Git to clone, and Python 3.8+ for the installer and linter. The Markdown skill itself has no runtime dependency. You can also download and extract a release ZIP instead of using Git.

## Install

From the repository root:

```bash
python scripts/install.py --agent codex --dry-run
python scripts/install.py --agent codex
# Or:
python scripts/install.py --agent claude
```

| Agent | Default destination |
| --- | --- |
| Codex | `$CODEX_HOME/skills/top-venue-paper-writing` if set, otherwise `~/.codex/skills/top-venue-paper-writing` |
| Claude Code | `~/.claude/skills/top-venue-paper-writing` |

`--dest` is the complete skill directory, not its parent:

```bash
python scripts/install.py --dest ./my-skills/top-venue-paper-writing
```

For a project-local installation, choose the skill directory recognized by your agent, for example `.claude/skills/top-venue-paper-writing` for Claude Code or `.agents/skills/top-venue-paper-writing` for Codex. Run this from the desired project or supply an absolute path.

The installer copies `SKILL.md`, `LICENSE`, `agents/`, `assets/`, `references/`, `templates/`, `examples/`, and `scripts/paperlint.py`. It does not install Git metadata, CI configuration, tests, or repository documentation. No package manager, network access, shell profile changes, or API keys are involved.

## Without the installer

Clone directly into a fresh skill folder. On macOS/Linux:

```bash
# Codex (use your configured CODEX_HOME if different)
git clone https://github.com/Shu-yin0/top-venue-paper-writing.git ~/.codex/skills/top-venue-paper-writing

# Or Claude Code
git clone https://github.com/Shu-yin0/top-venue-paper-writing.git ~/.claude/skills/top-venue-paper-writing
```

PowerShell:

```powershell
git clone https://github.com/Shu-yin0/top-venue-paper-writing.git "$HOME/.codex/skills/top-venue-paper-writing"
```

Alternatively, ask Codex's built-in `$skill-installer` to install the skill at the root of `https://github.com/Shu-yin0/top-venue-paper-writing` with the name `top-venue-paper-writing`.

## Verify discovery

Ask the agent to use `$top-venue-paper-writing` (Codex) or `/top-venue-paper-writing` (Claude Code) on a short section. If discovery has not refreshed, start a new session. The installed folder must contain `SKILL.md` directly, with no extra nested repository directory.

## Update

The copy installer deliberately refuses to overwrite existing files. Rename your installed folder to a backup, update your downloaded repository with `git pull --ff-only`, then run the installer again. Review any local changes before retiring the backup.

If you installed with a direct Git clone, run `git pull --ff-only` inside that installation. If it reports local changes or divergent history, review them rather than discarding them.

## 中文提示

- `--dry-run` 只显示计划，不创建安装目录。
- `--dest` 指向完整的 Skill 目录，不是它的上一级。
- 安装器不覆盖旧版本；更新前先备份原目录。
- Windows 可用 `py` 代替 `python`，macOS/Linux 可用 `python3`。
- 路径中有空格时，用引号包裹完整路径。
- 检查脚本主要面向英文；中文写作应使用章节指南，不能依赖英文词数统计。
