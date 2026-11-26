# Feedback Paths Studio

A working prototype for *Feedback Paths*, a Stanford master's research project by Rachel Zhao on how English learners engage with peer and AI feedback.

Students discuss peer and AI feedback on a draft. Every reply is coded for engagement, an explicit scaffolding policy picks the AI coach's next move and fades support, revisions are aligned to feedback, and an agency panel shows who is doing the thinking. A teacher dashboard shows feedback journeys with evidence.

- `claude-version/index.html`: the source. This is the classroom version that runs on claude.ai, with Claude as the coach and class submissions saved.
- `index.html`: the web demo with a rule-based coach, generated from the source. Static, no build step.
- `tools/build-web.py`: regenerates the web demo after editing the source:

  ```bash
  python3 tools/build-web.py claude-version/index.html index.html
  ```

Project page: https://feedback-paths.vercel.app
