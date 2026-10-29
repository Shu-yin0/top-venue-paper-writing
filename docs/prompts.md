# Prompt cookbook / 提示词集

Replace the filenames with your own and provide the referenced files. These prompts request editing or review, not invented experiments. In Codex use `$top-venue-paper-writing`; in Claude Code use `/top-venue-paper-writing`.

## 1. Rewrite an abstract / 改摘要

```text
Use $top-venue-paper-writing to rewrite abstract.tex for an empirical ML paper.
Preserve all numbers, datasets and protocol details. Make the problem,
method, evidence and scope clear. Flag unsupported claims separately.
Return the revised abstract and a concise edit rationale.
```

```text
使用 $top-venue-paper-writing 改写 abstract.tex。
保留所有数字、数据集与实验协议，讲清问题、方法、证据和适用范围。
将缺少支持的主张单独列出，交付改写版本和简短修改说明。
```

## 2. Audit the paper / 审全文

```text
Use $top-venue-paper-writing to audit main.tex with results/ as evidence.
Build a claim ledger, then prioritize problems by their effect on validity
and reader understanding. Do not change results or invent citations.
Return a section audit, proposed edits and an open-decisions list.
```

```text
使用 $top-venue-paper-writing 审校 main.tex，证据在 results/ 中。
建立主张台账，按对结论有效性和可读性的影响排序。
不要改动实验结果或编造引用。输出章节审校、修改建议和待决事项。
```

## 3. Draft from evidence / 从结果起草

```text
Use $top-venue-paper-writing with the supplied tables, figures and protocols.
Start with the claim ledger and identify missing evidence. Draft only
supported claims; leave explicit placeholders for unresolved details.
Begin with an outline and the experiments section.
```

```text
使用 $top-venue-paper-writing，根据所附表格、图和实验协议起草论文。
先做主张台账并列出证据缺口，只写已有证据支持的结论。
未确定的信息保留明确占位，先交付提纲和实验章节。
```

## 4. Submission review / 投稿前检查

```text
Use $top-venue-paper-writing for a submission review of main.tex, supp.tex
and submission.zip. The current venue requirements are in venue-rules.md.
Run the applicable paperlint checks, explain their findings and identify
what still needs manual inspection. Do not submit or upload the manuscript.
```

```text
使用 $top-venue-paper-writing 检查 main.tex、supp.tex 和 submission.zip。
本届会议要求见 venue-rules.md。运行适用的 paperlint 检查，
解释命中项，并列出仍需人工检查的内容。不要代替我投稿或上传稿件。
```

## 5. Remove vague prose / 清理空泛表达

```text
Use $top-venue-paper-writing to edit this section for specificity and flow.
Keep technical terms and meaningful uncertainty. Remove filler only when
it adds no information. Do not treat word-list matches as an AI detector.
Show a before/after comparison for the most consequential edits.
```

```text
使用 $top-venue-paper-writing 提高这一节的具体性和连贯性。
保留技术术语和有意义的不确定性，只删除不提供信息的套话。
不要把词表当作 AI 检测器。对主要修改给出前后对照。
```
