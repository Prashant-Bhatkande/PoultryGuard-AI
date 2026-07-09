# Rule Engine

Version: 1.0

---

Purpose

The Rule Engine receives information from every AI module.

It decides whether the loading process is correct.

The Rule Engine never processes images.

It only evaluates events.

---

Inputs

Bird Detection

Bird Tracking

OCR

Camera Status

Time

Configuration

---

Outputs

Normal Event

Warning

Critical Event

Dashboard Alert

Phone Notification

Video Clip

Database Record

---

Loading Workflow

EMPTY

↓

BIRDS_LOADED

↓

WAITING_FOR_DONE

↓

DONE_DETECTED

↓

BIRDS_LEAVING

↓

BATCH_COMPLETE

---

Critical Rule

Birds must NOT leave the weighing platform before DONE is detected.

---

Important Design Decision

0.00 is NOT required.

Reason

Workers sometimes load the next batch immediately.

The system tracks bird movement instead of depending on seeing 0.00.

---

Every Event Stores

Timestamp

Camera

Bird Count

OCR Result

Confidence

Video Clip

Database ID