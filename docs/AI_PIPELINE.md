# AI Pipeline

Version: 1.0

---

# Vision Engine

The Vision Engine is responsible for understanding everything happening in front of the cameras.

It does NOT make business decisions.

It only observes and reports.

---

# Processing Pipeline

Camera

↓

Frame Capture

↓

Image Preprocessing

↓

Bird Detection

↓

Bird Tracking

↓

OCR

↓

Vision Results

↓

Rule Engine

---

# Image Preprocessing

Purpose

Improve image quality before AI processing.

Tasks

Resize

Noise Reduction

Brightness Adjustment

Contrast Adjustment

ROI Cropping

Frame Timestamp

---

# Bird Detection

Purpose

Detect birds.

Output

Bounding Boxes

Confidence

Class

---

# Bird Tracking

Purpose

Assign temporary IDs to birds.

Output

Bird ID

Movement

Speed

Direction

---

# OCR

Purpose

Read the weight machine display.

Output

Weight

DONE

Batch Number

Confidence

---

# Vision Results

The Vision Engine sends only structured data.

Example

Bird Count: 25

DONE: TRUE

Weight: 615.3

Batch: 1458

Confidence: 99.4%

Timestamp:
22:14:15

The Rule Engine decides what this means.