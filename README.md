
# 2026-Season

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/BC-Robotics-4504/2026-Season/ci.yml?branch=main)
![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)

## Overview
This repository contains the codebase for BC Robotics Team 4504's 2026 season robot, written in Python using the RobotPy project and the WPILib command-based framework. The repository is designed for rapid onboarding and collaborative development, with a dev container setup for a consistent environment. All robot logic, subsystems, and commands follow the WPILib command-based structure for maintainability and ease of use.


## Getting Started

If you need help setting up Dev Containers, refer to the guide at [docs.bcr4504.org](https://docs.bcr4504.org).

1. **Clone the repository:**

	```sh
	git clone https://github.com/BC-Robotics-4504/2026-Season.git
	```

2. **Open in VS Code:**

	- Make sure you have the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.
	- Open the folder in VS Code.
	- When prompted, "Reopen in Container" to automatically set up the environment.

3. **Start coding!**

	- The Python environment, shell, and all tools will be ready to use.

## Repository Structure
- `robot.py`, `robotcontainer.py`: Main robot code
- `constants.py`: Project-wide constants
- `commands/`, `subsystems/`: Modular code organization
- `deploy/`: Deployment assets (paths, autos, navgrid)
- `tests/`: Test suite
- `.devcontainer/`: Dev container configuration

## Onboarding Checklist
- [ ] Clone the repo and open in VS Code
- [ ] Reopen in container
- [ ] Review the code structure
- [ ] Run tests (`pytest` or via VS Code)
- [ ] Read and follow team coding standards

## License
This project is licensed under the GNU General Public License v2. See [LICENSE.txt](LICENSE.txt) for details.

---
For questions or help, contact a team lead or open an issue on GitHub.
