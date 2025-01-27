# Netzer 🌐

## About
A forgotten network analysis project from 2023

Version: Beta 0.1

## Features
- 🔍 Active host discovery using Nmap
- 📡 Automatic interface detection
- 🏷️ Hostname resolution
- 🖥️ Network interface management
- 📊 Clean tabulated output
- 🎨 Color-coded terminal interface

## Prerequisites
```bash
python3
python3-pip
nmap
```

## Installation
```bash
# Clone the repository
git clone https://github.com/vixhnuchandran/Netzer.git

# Navigate to the directory
cd Netzer

# Install required packages
pip install -r requirements.txt
```

## Usage
```bash
python3 netzer.py
```

The tool will:
1. Display available network interfaces
2. Allow you to select your preferred interface
3. Scan the network for active hosts
4. Display results in a formatted table

## Sample Output
```
░░░░░░░░░░░░░░░░░░░░░░░░░░░░
[+] ACTIVE INTERFACES:
╒══════════╤═══════════════╕
│Interface │ Address       │
╞══════════╪═══════════════╡
│wlan0     │ 192.168.1.100 │
└──────────┴───────────────┘

[+] AVAILABLE TARGETS:
╒══════════════╤═══════════════╕
│ Active Host  │ Hostname      │
╞══════════════╪═══════════════╡
│192.168.1.1   │ router.local  │
│192.168.1.100 │ mypc.local    │
└──────────────┴───────────────┘
```

## Project Structure
```
netzer/
├── core/
│   ├── colours.py    # Terminal color definitions
│   ├── info.py       # Network information gathering
│   └── hostdiscovery.py  # Host scanning functionality
└── netzer.py         # Main application
```


## Future Improvements
- [ ] Extended subnet range support
- [ ] Port scanning capabilities
- [ ] Service detection
- [ ] Custom scan options
- [ ] Export results to multiple formats
