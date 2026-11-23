# 🩹 Self-Healing CI/CD Pipeline

> **Winner of the Wakanda Data & Captain Code Awards** (Hopefully!) 🏆

A fully autonomous DevOps agent that detects CI/CD failures, performs Root Cause Analysis (RCA) using **Google Gemini 2.0 Flash**, and automatically generates code fixes validated by **CodeRabbit**.

## 🏗 Architecture 

1.  **Failure Detection:** GitHub Actions triggers a webhook upon pipeline failure.
2.  **Orchestration:** **Kestra** receives the signal and starts the recovery flow.
3.  **Analysis:** **Gemini 2.0** analyzes the logs + source code to identify the root cause.
4.  **Repair:** The agent creates a fix, pushes a new branch, and opens a PR.
5.  **Validation:** **CodeRabbit** reviews the fix for quality assurance.

## 📂 Project Structure

* `src/`: The application source code (e.g., `calc.py`).
* `tests/`: Pytest suites designed to catch regressions.
* `kestra/flows/`: The orchestration logic (YAML definitions).
* `.github/workflows/`: The CI pipeline configuration.

## 🚀 How to Run the Demo

1.  **Introduce a Bug:**
    Modify `src/calc.py` to break logic (e.g., change `+` to `-`).
    
2.  **Push to Main:**
    ```bash
    git commit -am "Oops, broken code"
    git push origin main
    ```

3.  **Watch the Magic:**
    * Go to the **Actions** tab to see the failure.
    * Go to **Pull Requests** to see the AI agent open a fix automatically!

## 🛠 Tech Stack

* **Orchestration:** Kestra
* **AI:** Google Gemini 2.0 Flash
* **CI:** GitHub Actions
* **Quality:** CodeRabbit
