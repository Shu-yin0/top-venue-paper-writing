<p align="center"><img src="assets/banner.png" alt="CCF-A 论文写作 — 从实验依据到清晰的论文" width="100%"></p>

<p align="center">
  <a href="https://github.com/Shu-yin0/top-venue-paper-writing/actions/workflows/ci.yml"><img src="https://github.com/Shu-yin0/top-venue-paper-writing/actions/workflows/ci.yml/badge.svg?branch=main" alt="自动检查"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-264D42?style=flat-square" alt="MIT 许可"></a>
  <a href="https://github.com/Shu-yin0/top-venue-paper-writing/releases"><img src="https://img.shields.io/badge/release-v1.1.1-264D42?style=flat-square" alt="最新版本"></a>
  <img src="https://img.shields.io/badge/Python-3.8%2B-264D42?style=flat-square" alt="Python 3.8 及以上">
</p>

<p align="center"><a href="README.md">English</a> · <b>简体中文</b></p>
<p align="center"><a href="#快速开始">快速开始</a> · <a href="#四种工作模式">工作模式</a> · <a href="docs/prompts.md">提示词示例</a> · <a href="examples/rewrites.md">改写示例</a></p>

# CCF-A 论文写作

**把实验依据，写成主张清楚、证据扎实的机器学习论文。**

一个面向 CCF-A 会议与期刊投稿的论文写作 Skill，当前重点支持机器学习与计算机视觉领域的实证论文。它从「主张—证据台账」出发，按需处理各个章节，最后用可重复运行的检查辅助投稿准备。

支持 **Codex 与 Claude Code**，也可以直接当作人工写作检查清单使用。写作指南适用于中文和英文；附带的检查工具主要面向英文及 LaTeX/Markdown 源文件。脚本无需 API Key，无需第三方 Python 依赖。

> 这是写作方法与辅助工具，不承诺录用，也不代表任何会议的官方要求。实际投稿时，以目标会议当年的规则为准。

## 它解决什么问题

| 先核对证据 | 按实际需要改稿 | 用脚本辅助检查 |
| --- | --- | --- |
| 每条主张对应指标、实验协议和证据位置。 | 可以写整篇，也可以只审一段摘要或引言。 | 检查重复表达、强结论用词、补充材料引用和潜在身份泄露。 |

## 快速开始

**1. 下载仓库**

```bash
git clone https://github.com/Shu-yin0/top-venue-paper-writing.git
cd top-venue-paper-writing
```

**2. 安装到使用的工具**

```bash
# Codex
python scripts/install.py --agent codex

# 或 Claude Code
python scripts/install.py --agent claude
```

macOS/Linux 没有 `python` 时用 `python3`；Windows 也可使用 `py`。安装器只复制 Skill 所需文件，打印安装位置，并拒绝覆盖已有安装。可加 `--dry-run` 预览，或通过 `--dest PATH` 指定目标目录。详见[安装与更新](docs/installation.md)。

**3. 给它一个具体任务**

在 Codex 中：

```text
使用 $top-venue-paper-writing 审校我的引言。
保留原有技术含义，不新增未经验证的结论。
请给出改写版本、证据缺口，以及主要修改理由。
```

在 Claude Code 中：

```text
/top-venue-paper-writing 帮我改写这段摘要，保留实验数字、
数据集与实验协议，标出缺少依据的表述，不虚构引用。
```

同时提供稿件与已有证据文件。安装后如果没有立即识别到 Skill，可新开一个会话，也可让助手直接读取 [SKILL.md](SKILL.md)。

## 四种工作模式

| 模式 | 你提供 | 它交付 |
| --- | --- | --- |
| **起草 Draft** | 实验结果、图表、目标会议 | 主张台账、证据缺口、分章节草稿 |
| **审校 Audit** | 已有论文 | 按优先级排列的审校意见、修改建议、待决事项 |
| **局部改写 Rewrite** | 一个章节与需保留的结论 | 聚焦改写、修改理由、结论适用范围 |
| **投稿检查 Submission** | 正文、补充材料、会议要求 | 源文件检查、未解决问题、外部冷读提纲 |

```text
实验依据 → 主张台账 → 按需修改章节 → 全文复核 → 投稿检查
```

[打开中英文提示词集 →](docs/prompts.md)

## 30 秒试用检查工具

```bash
python scripts/paperlint.py words examples/demo-paper.tex --lists ai,risk
```

示例是明确标注的虚构内容，故意保留了 `leverage` 和 `outperforms` 两处待审查表达。实际输出会给出文件名、行号和上下文。

| 命令 | 用途 |
| --- | --- |
| `length` | 按默认预算检查摘要、结论字数 |
| `words` | 标记风格词、需要证据的强结论与模糊措辞 |
| `overlap` | 检查两个文件或两个章节的连续重复词组 |
| `suppmap` | 核对 `Supp.~S1` 形式的引用与补充材料章节 |
| `anon` | 检查文本、文件名与基础 PDF 元数据中的身份线索 |

退出码：`0` 无发现，`1` 有待审查项，`2` 输入或命令错误。出现命中不等于写错，没有命中也不等于可以直接投稿。PDF 检查不解析完整正文、压缩对象或图片文字。详见 [CLI 文档](docs/paperlint.md)。

## 仓库内容

- [SKILL.md](SKILL.md)：使用入口、模式选择和基本约束。
- [references/](references/)：11 份主题指南，覆盖主张、各章节、图表、全文、投稿与来源说明。
- [templates/](templates/)：主张台账、章节审校、待决事项、修改记录、冷读提纲。
- [examples/rewrites.md](examples/rewrites.md)：标注为虚构的改写前后示例。
- [docs/prompts.md](docs/prompts.md)：可复制使用的中英文任务提示词。
- [scripts/](scripts/)：安装器、论文检查工具与 Skill 结构校验。
- [tests/](tests/)：脚本回归测试，GitHub Actions 在 Linux/Windows 上运行。

## 使用边界

不虚构实验、数据、引用或统计支持。作者决定最终表达，但文字润色不能隐藏会改变结论的重要反证或适用条件。没有证据时，缩小主张或列为待决事项。只改一个章节时，不强制启动整篇论文流程。

写作规则来自随原始压缩包提供的经验指南；其中的使用经历没有在本仓库中独立复核。参见[来源与局限](references/sources-and-evidence.md)。

## 开发与贡献

```bash
python -m unittest discover -s tests -v
python scripts/validate_skill.py
```

[贡献说明](CONTRIBUTING.md) · [更新记录](CHANGELOG.md) · [MIT 许可](LICENSE)
