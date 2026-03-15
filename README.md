# Military Readiness & Human Performance Tracker

A Python command-line application for tracking personnel readiness and fitness test scores across military units. Built on real operational experience supporting **USSOCOM** and **U.S. Air Force Special Operations** personnel.

---

## Overview

This tool models the actual unit hierarchy used in military organizations — Unit → Flight → Operator — and implements the real **USAF Special Warfare fitness test scoring system** to calculate and track individual and collective readiness.

Designed with the same data-driven approach used in real human performance programs: track who is mission ready, who is not, and why.

---

## Features

- **Full unit hierarchy** — organize personnel by unit, flight, and individual operator
- **Real USAF SW fitness test scoring** — point-based system with auto-fail logic based on actual standards
- **Automated score calculation** — enter raw performance data, points calculated automatically
- **Readiness tracking** — GREEN/RED status per operator based on DNIC and PT clearance
- **Flight and unit analytics** — average scores and readiness rates at both levels
- **Persistent storage** — all data saved and loaded from JSON
- **Full CLI** — intuitive menu-driven interface for unit, flight, and operator management

---

## Fitness Test Events

The USAF Special Warfare fitness test is scored out of **100 points**. An auto-fail on any single event results in an overall test failure regardless of total score.

| Event | Max Points | Metric |
|---|---|---|
| 3 Mile Ruck | 20 | Time (seconds) |
| Standing Long Jump | 10 | Distance (inches) |
| Pro Agility Right | 5 | Time (seconds) |
| Pro Agility Left | 5 | Time (seconds) |
| Trap Bar Deadlift | 10 | Weight (lbs) |
| Pull-ups | 10 | Reps |
| Farmers Carry | 10 | Time (seconds) |
| Shuttle Run Repeat | 10 | Time (seconds) |
| Combat Run 1.5mi OR Swim 1500m | 20 | Time (seconds) |

> Operators choose run or swim each year but cannot repeat the same choice two consecutive years.

---

## Project Structure

```
readiness_tracker/
├── main.py              # CLI entry point and menu system
├── sw_operator.py       # Operator class with fitness test logic
├── flight.py            # Flight class — manages a group of operators
├── unit.py              # Unit class — manages a group of flights
├── scoring_tables.py    # USAF SW fitness test scoring tables
├── data_manager.py      # JSON save/load functionality
└── readiness_data.json  # Persistent data file (auto-generated)
```

---

## Usage

```bash
python main.py
```

On first run you will be prompted to create a unit. From there you can add flights, add operators, record fitness test scores, and view readiness reports.

### Main Menu
```
1. Unit commands      — view averages, readiness, manage flights
2. Flight commands    — manage operators, view flight stats
3. Operator commands  — record tests, update status, view scores
4. Save and exit
```

---

## Example Output

```
Unit Readiness: 78.3%
Unit Average Score: 84.2

Alpha Flight readiness: 66.7%
Alpha Red Operators: {'martinez': {...}, 'okonkwo': {...}}

Name: Johnson
Rank: SSgt
Unit: 7th ASOS
Flight: Alpha
Medical Status: GREEN
PFT: PASS
```

---

## Tech Stack
- Python 3
- `json` for data persistence
- Object-oriented design across 5 modules
- Real USAF SW fitness test standards

---

## Background

Built from firsthand experience designing and managing human performance programs for **200+ U.S. Air Force and USSOCOM Special Operations personnel**. The scoring system, unit hierarchy, and readiness criteria reflect actual operational standards used in special operations environments.

---