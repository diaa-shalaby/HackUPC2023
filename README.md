# HackUPC2023
Our group's repo for the HackUPC challenge 2023

## :file_folder: Table of Contents
- [eyes-spies](https://github.com/gorbe2002/eyes-spies#eyes-spies)
- [:clipboard: Table of Contents](https://github.com/gorbe2002/eyes-spies#clipboard-table-of-contents)
- [:thought_balloon: Introduction to CLI and CLI tools](https://github.com/gorbe2002/eyes-spies#thought_balloon-introduction-to-cli-and-cli-tools)
- [:memo: Description](https://github.com/gorbe2002/eyes-spies#memo-description)
- [:open_book: Commands](https://github.com/gorbe2002/eyes-spies#open_book-commands)
- [:microscope: Technologies](https://github.com/gorbe2002/eyes-spies#microscope-technologies)
- [:mag: In-Depth](https://github.com/gorbe2002/eyes-spies#mag-in-depth)
- [:blue_book: Technical Details](https://github.com/gorbe2002/eyes-spies#blue_book-technical-details)

## :thought_balloon: Introduction to CLI and CLI tools
- CLI stands for Command Line Interface, which is a way of interacting with a computer program or operating system using text commands typed into a terminal or command prompt. A CLI allows users to execute commands, navigate directories, and perform various tasks using keyboard input, instead of using a graphical user interface (GUI) that relies on mouse clicks and icons.
- CLI tools are software programs that are designed to be used from the command line. They are usually lightweight and faster than their GUI counterparts, making them popular among developers and system administrators. CLI tools can be used to perform a wide range of tasks, such as text processing, file manipulation, system monitoring, network diagnostics, and more.

## :memo: Description
In this project, we created multiple CLI tools, which can range from showing you the weather forecast, to creating an ascii art video. Now you might wonder where Ice Spice fits into all of this. It's simple, she inpired the idea to create the munch CLI tool.

## :open_book: Commands
- [Help](https://github.com/gorbe2002/eyes-spies/wiki#help)
- [Weather](https://github.com/gorbe2002/eyes-spies/wiki#weather)
- [Dance](https://github.com/gorbe2002/eyes-spies/wiki#dance)
- [Logo](https://github.com/gorbe2002/eyes-spies/wiki#logo)
- [Text](https://github.com/gorbe2002/eyes-spies/wiki#text)
- [Name Servers](https://github.com/gorbe2002/eyes-spies/wiki#name-servers)
- [IP](https://github.com/gorbe2002/eyes-spies/wiki#ip)
- [Operating System](https://github.com/gorbe2002/eyes-spies/wiki#operating-system)

## :microscope: Technologies
- Language(s): `go`, `html`, `css`, `python`
- Technologies: `nginx`, `GCP`

### :mag: In-Depth
<!-- Github -->
<details>
	<summary>Github</summary>

- Projects

- Issues

- Code (Source Code)

- CODEOWNERS

- Branch Protections

- Wiki

- Dependency Graph (Exported SBOM to do some analysis)

- CITATIONS

- SECURITY Policy

- Code of Conduct

</details>

<!-- Domain.com -->
<details>
	<summary>Domain.com</summary>

- Custom Nameservers to Google Cloud Platform

- Our Spice-y domain: http://espies.tech/. Check it out!

</details>

<!-- Twilio -->
<details>
	<summary>Twilio</summary>

- Send SMS

</details>

<!-- GCP -->
<details>
    <summary>Google Cloud Platform</summary>

- Compute Engine

    - VM Instances

- Network Services

    - Cloud DNS

- IAM & Admin

    - IAM

    - Identity & Organization

    - Service Accounts

- VCP Network

    - IP Addresses

    - Shared VPC

</details>

## :blue_book: Technical Details
- Need a `.env` file in root directory of this program with the following fields:
```txt
# Enter values where `<>` is
M_PHONE="<>"
TWILIO_ACCOUNT_SID="<>"
TWILIO_AUTH_TOKEN="<>"
```

- Dance will not work out of the gate (unfortunately), however this can be ameliorate by doing the following:
1. [Download munch.gif](https://drive.google.com/u/1/uc?id=1FFX4jj5EMxLRmfuZ6-LGJpG6RaSfMQz2&export=download)
1. Put `munch.gif` in `vid` Directory
1. Test it out! `./munch dance`
