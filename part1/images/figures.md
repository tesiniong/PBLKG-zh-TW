# 第一部分 圖片對照清單（part1 figures）

來源：`pdf/Praktinė_gramatika_fixed.pdf`（PDF 頁碼 = 書印刷頁碼 + 1）。
圖檔統一編號 `fig1.png`–`fig8.png`，存於 `part1/images/`。
嵌入語法（章節 md 與 images/ 同在 part1/，用相對路徑）：

```markdown
![圖N](images/figN.png)

**圖N.** 圖說……
```

| 圖 | 檔案 | PDF頁 | 立陶宛語圖說（原書） | 所屬章節 | 狀態 |
|---|---|---|---|---|---|
| 圖1 | fig1.png | 20 | 1 pav. Kalbos padargai | 3-語音學的分支 | ✅ 已嵌入 |
| 圖2 | fig2.png | 22 | 2 pav. Profilinis kalbos padargų vaizdas, artikuliuojant balsius i (kairėje) ir a | 3-語音學的分支 | ✅ 已嵌入（左右兩圖已合併）|
| 圖3 | fig3.png | 24 | 3 pav. Žodžio tiki̇̀ oscilograma | 3-語音學的分支 | ✅ 已嵌入 |
| 圖4 | fig4.png | 25 | 4 pav. Žodžio tiki̇̀ spektrograma | 3-語音學的分支 | ✅ 已嵌入 |
| 圖5 | fig5.png | 35 | 5 pav. Lietuvių kalbos balsių planimetrinis modelis | 4-元音 | ⏳ 待該章翻譯後嵌入（向量圖，已 300dpi 渲染裁切）|
| 圖6 | fig6.png | 38 | 6 pav. Lietuvių kalbos balsių vidutinės formančių reikšmės (šaltinis: Girdenis A. …) | 4-元音 | ⏳ 待嵌入 |
| 圖7 | fig7.png | 59 | 7 pav. Fonologinė balsių sistema: dendrograma (šaltinis: Girdenis A. Teoriniai fonologijos pagrindai. Vilnius: Petro ofsetas, 1995, p. 168) | 4-元音 | ⏳ 待嵌入（純向量圖，已 300dpi 渲染裁切）|
| 圖8 | fig8.png | 72 | 8 pav. Kirčiuotų [uɔ], [ɑˑɪ] formantės (moters balsas) | 6-二合音核 | ⏳ 待嵌入（左右兩圖已合併）|

## 備註
- 圖內標籤維持立陶宛語原文，譯文比照第3章圖3做法，列在圖說下方。
- 圖5、圖7 在原書是向量繪圖，無法用 `pdfimages` 抽出，改以整頁 300dpi 渲染後裁切，畫質優於內嵌點陣圖。
- 圖2、圖8 在原書為左右並排兩張影像，已合併為單一圖檔。
- 重新產生流程：`pdfimages -all -f <頁> -l <頁> 全書.pdf out`（點陣圖）；向量圖用 `pdftoppm -png -r 300 -f <頁> -l <頁>` 再裁切。
