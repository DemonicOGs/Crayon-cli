# Crayon

### Local AI Coding CLI

Crayon is a local-first AI coding CLI designed to bring AI-assisted development directly into the terminal.

It combines a TypeScript/Node.js CLI with local AI inference, development tools, streaming responses, multimodal capabilities, project instructions, and local model management.

---

## 🚀 Features

- 🤖 Local AI inference
- 🧠 Google Gemma support
- 🐍 Python + Transformers model runtime
- ⚡ FastAPI inference server
- 🌊 Streaming responses
- 🖼️ Image understanding
- 🎵 Audio understanding
- 🎥 Video understanding
- 🧩 Multimodal prompts
- 📁 File-system tools
- 💻 Terminal command execution
- 🔎 Project/code search
- 📝 Project instructions with `AGENTS.md`
- 🧠 Conversation memory
- 🔧 Runtime configuration
- 📊 Server diagnostics
- 🌐 Cross-platform CLI architecture

---

# 📦 Architecture

```text
                         ┌─────────────────────┐
                         │       Crayon        │
                         │    CLI / Terminal   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Node.js / TS      │
                         │   Agent Runtime     │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
              File System      Terminal         Search
                 Tools           Tools            Tools
                    │               │                │
                    └───────────────┼────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Local AI Provider │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Server    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Transformers      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                                  Gemma
```

---

# 🛠️ Technology Stack

## CLI

- Node.js
- TypeScript
- npm

## Local AI Runtime

- Python
- FastAPI
- PyTorch
- Hugging Face Transformers
- Google Gemma

## Development Tools

- File-system operations
- Terminal execution
- Project search
- Agent instructions

---

# 📚 Release History

## v0.1.0 — Initial CLI Foundation

The first Crayon CLI foundation.

### Included

- Interactive CLI
- Agent architecture
- File-system tools
- Terminal tools
- Search tools
- Provider architecture
- Initial AI provider support
- CLI setup functionality

---

## v0.2.0 — Local Gemma + FastAPI + Transformers

Introduced the first local AI runtime.

### Included

- Local Gemma support
- Python model backend
- FastAPI inference server
- Transformers integration
- Local model inference
- Node.js → FastAPI communication

### Architecture

```text
Crayon
   │
   ▼
Node.js
   │
   ▼
FastAPI
   │
   ▼
Transformers
   │
   ▼
Gemma
```

---

## v0.3.0 — Streaming Inference

Introduced real-time AI response streaming.

### Included

- `TextIteratorStreamer`
- FastAPI `StreamingResponse`
- Background model generation
- Node.js response streaming
- Progressive CLI output

### Architecture

```text
Gemma
  │
  ▼
TextIteratorStreamer
  │
  ▼
FastAPI StreamingResponse
  │
  ▼
Node.js Reader
  │
  ▼
Crayon CLI
```

Responses can appear progressively instead of waiting for the entire generation.

---

## v0.4.0 — Multimodal AI

Expanded Crayon beyond text-only AI.

### Supported Inputs

```text
Text
Image
Audio
Video
Text + Media
Multiple Media
```

### Architecture

```text
                 ┌──────────┐
                 │  Text    │
                 └────┬─────┘
                      │
                 ┌────▼─────┐
                 │  Image   │
                 └────┬─────┘
                      │
                 ┌────▼─────┐
                 │  Audio   │
                 └────┬─────┘
                      │
                 ┌────▼─────┐
                 │  Video   │
                 └────┬─────┘
                      │
                      ▼
               Multimodal Model
                      │
                      ▼
                   Response
```

---

## v0.4.1 — Help UI

Introduced the structured Crayon help interface.

### Included

```text
/help
/status
/models
/clear
/search
/image
/audio
/video
/run
/exit
```

The CLI received a dedicated interactive help interface for discovering available commands and capabilities.

---

## v0.5.0 — Expanded CLI

Expanded Crayon into a more complete coding-agent CLI.

### Included

- Expanded interactive commands
- Local AI workflow improvements
- Development tools
- Multimodal commands
- Conversation handling
- Model/server interaction
- Improved CLI structure

---

## v0.5.1 — AGENTS.md Support

Introduced project-level and global agent instructions.

### Included

- `AGENTS.md`
- Project instructions
- Global instructions
- `/init`
- `/init --global`
- `/agent`
- Automatic instruction injection

### Instruction Hierarchy

```text
Global Instructions
        │
        ▼
Project Instructions
        │
        ▼
Current Project
        │
        ▼
AI Agent
```

---

## v0.5.2 — Local Server Management

Improved local model-server management and diagnostics.

### Included

- Local server startup
- Server readiness detection
- Health checks
- Model discovery
- Server diagnostics
- `/status`
- `/models`
- `/clear`
- Configurable host/port
- Server startup control

### Environment Variables

```env
AGY_HOST=127.0.0.1
AGY_PORT=8765
AGY_START_SERVER=true
```

---

## v0.5.3 — Local Runtime Stabilization

Focused on stabilizing the local Gemma runtime and finalizing the CLI help experience.

### Included

- Local Gemma runtime improvements
- FastAPI runtime stabilization
- Provider improvements
- Server communication fixes
- Streaming improvements
- Finalized help UI
- Improved local inference reliability

### Supported Capabilities

```text
Text → Text
Image → Text
Audio → Text
Video → Text
Text + Media → Text
Multiple Media → Text
```

---

## v0.5.4 — Expanded Development Commands

Introduced additional CLI functionality.

### New Commands

```text
/config
/media
/read
```

Along with the existing commands:

```text
/help
/status
/models
/clear
/init
/init --global
/agent
/search
/image
/audio
/video
/run
/exit
```

The release also cleaned up the help interface and removed the old fake "One-shot" section.

---

# 💻 CLI Commands

```text
/help
/status
/models
/clear
/config
/media
/read
/init
/init --global
/agent
/search <text>
/image <file> <question>
/audio <file> <question>
/video <file> <question>
/run <command>
/exit
```

---

# 🧠 Local AI

Crayon is designed around local inference.

The local architecture is:

```text
Crayon CLI
     │
     ▼
Node.js
     │
     ▼
Python FastAPI
     │
     ▼
PyTorch
     │
     ▼
Transformers
     │
     ▼
Local Model
```

Model files can be obtained through the Hugging Face ecosystem, while inference is performed locally through the Python runtime.

---

# 🌊 Streaming

Crayon supports streaming AI responses.

The local text runtime uses:

```text
TextIteratorStreamer
```

and:

```text
FastAPI StreamingResponse
```

The CLI receives generated text progressively.

---

# 🖼️ Multimodal AI

Crayon supports multimodal interactions.

### Image

```text
/image image.png What is in this image?
```

### Audio

```text
/audio recording.wav Summarize this audio.
```

### Video

```text
/video video.mp4 Describe what happens in this video.
```

---

# 📁 Project Instructions

Crayon supports `AGENTS.md`.

Initialize project instructions:

```text
/init
```

Initialize global instructions:

```text
/init --global
```

Inspect the active agent configuration:

```text
/agent
```

---

# 🔧 Configuration

Crayon supports environment-based configuration.

Example:

```env
AGY_HOST=127.0.0.1
AGY_PORT=8765
AGY_START_SERVER=true
```

Configuration can be inspected through:

```text
/config
```

---

# 🩺 Diagnostics

Check the local environment:

```text
/status
```

View available models:

```text
/models
```

---

# 🖥️ Cross-Platform

Crayon is designed to work across:

- Windows
- Linux
- macOS

The CLI is based on Node.js/TypeScript while the local AI runtime uses Python.

---

# 📦 Installation

Install Crayon globally:

```bash
npm install -g crayon-cli
```

Verify:

```bash
crayon --version
```

Start Crayon:

```bash
crayon
```

---

# 🛠️ Development

Clone the repository:

```bash
git clone https://github.com/DemonicOGs/Crayon-cli.git
```

Enter the project:

```bash
cd Crayon-cli
```

Install dependencies:

```bash
npm install
```

Build:

```bash
npm run build
```

Run:

```bash
npm start
```

---

# 📂 Project Structure

```text
crayon-cli/
├── src/
│   ├── agent/
│   ├── cli/
│   ├── providers/
│   └── tools/
│
├── dist/
│   ├── agent/
│   ├── cli/
│   ├── providers/
│   └── tools/
│
├── model/
│   └── server.py
│
├── AGENTS.md
├── package.json
├── tsconfig.json
└── README.md
```

---

# 🔐 Local-First Design

Crayon's core AI workflow is designed around local inference.

```text
Your Machine
┌──────────────────────────────┐
│                              │
│  Crayon                      │
│    │                         │
│    ▼                         │
│  Local Runtime               │
│    │                         │
│    ▼                         │
│  Local AI Model              │
│                              │
└──────────────────────────────┘
```

---

# 📜 Version Timeline

```text
v0.1.0
  │
  └── Initial CLI Foundation
          │
v0.2.0
  │
  └── Local Gemma + FastAPI + Transformers
          │
v0.3.0
  │
  └── Streaming Inference
          │
v0.4.0
  │
  └── Multimodal AI
          │
v0.4.1
  │
  └── Help UI
          │
v0.5.0
  │
  └── Expanded CLI
          │
v0.5.1
  │
  └── AGENTS.md Support
          │
v0.5.2
  │
  └── Local Server Management
          │
v0.5.3
  │
  └── Local Runtime Stabilization
          │
v0.5.4
  │
  └── Expanded Development Commands
```

---

# 📋 Release Summary

| Version | Release |
|---|---|
| `v0.1.0` | Initial CLI Foundation |
| `v0.2.0` | Local Gemma + FastAPI + Transformers |
| `v0.3.0` | Streaming Inference |
| `v0.4.0` | Multimodal AI |
| `v0.4.1` | Help UI |
| `v0.5.0` | Expanded CLI |
| `v0.5.1` | AGENTS.md Support |
| `v0.5.2` | Local Server Management |
| `v0.5.3` | Local Runtime Stabilization |
| `v0.5.4` | Expanded Development Commands |

---

# 📄 License

See the `LICENSE` file included with the project.

---

## Crayon

**Local AI. Coding. Tools. One CLI.**

```text
CRAYON
Local AI Coding CLI
```
