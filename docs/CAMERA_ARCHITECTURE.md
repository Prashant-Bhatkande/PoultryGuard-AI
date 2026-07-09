# Camera Architecture

Version: 1.0

---

## Camera Roles

### WEIGHT_MACHINE

Purpose

Read:
- DONE
- Weight
- Batch Number

AI Modules

- OCR

Priority

Critical

---

### OVERHEAD

Purpose

Monitor birds on weighing platform.

AI Modules

- Bird Detection
- Bird Tracking

Priority

Critical

---

### DOOR

Purpose

Monitor birds entering and leaving.

AI Modules

- Detection
- Tracking

Priority

High

---

### FARM

Purpose

Monitor returned birds.

AI Modules

- Detection
- Tracking

Priority

Medium

---

# Camera Sources

Supported

USB Camera

IP Camera

RTSP

Video File (Simulation)

Future

PoE Cameras

---

# Camera States

DISCONNECTED

CONNECTING

CONNECTED

STREAMING

RECORDING

ERROR

RECONNECTING

---

# Camera Configuration

Each camera has:

Camera ID

Role

Source

Resolution

FPS

Recording Enabled

Health Status

---

# Responsibilities

Camera

Connect

Disconnect

Read Frames

Return Camera Information

Camera Manager

Start Cameras

Stop Cameras

Monitor Cameras

Reconnect Cameras

Recorder

Save Video

Create Event Clips

Delete Old Videos

Health Monitor

FPS

Connection

Latency

Recording Status

Storage