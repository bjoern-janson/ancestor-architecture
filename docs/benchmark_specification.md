# Ancestor Architecture: Benchmark Specification

## Purpose

This document defines a proposed evaluation framework for measuring whether an intelligence system functions as:

- a substitution engine
- an optimization engine
- an amplification engine
- an ancestor architecture

The benchmark evaluates not only what a system produces, but what capability remains after the system is removed.

---

# 1. Core Benchmark Principle

Traditional evaluation:

\[
\boxed{
AI\ performance = quality\ of\ output
}
\]

Ancestor evaluation:

\[
\boxed{
AI\ performance =
quality\ of\ output
+
quality\ of\ capability\ transfer
}
\]

The primary question:

\[
\boxed{
After interaction, is the human or downstream system more capable without assistance?
}
\]

---

# 2. Benchmark Architecture

The benchmark contains five dimensions:

\[
\boxed{
B_{ancestor}
=
(C_t \times A_t \times P_M \times D \times E)
}
\]

Where:

| Symbol | Dimension |
|---|---|
| \(C_t\) | Capability transfer |
| \(A_t\) | Agency preservation |
| \(P_M\) | Model permeability |
| \(D\) | Diversity preservation |
| \(E\) | Exploration capacity |

---

# 3. Capability Transfer Benchmark

## Goal

Measure whether assistance produces lasting improvement.

---

## Experimental Setup

Participants complete:

1. baseline task
2. AI-assisted learning phase
3. independent evaluation
4. novel transfer task

---

## Measurements

### Assisted Performance

\[
P_{assist}
\]

Performance with AI support.

---

### Independent Performance

\[
P_{alone}
\]

Performance without AI.

---

### Transfer Performance

\[
P_{transfer}
\]

Performance on a structurally similar but novel task.

---

## Agency Transfer Score

\[
\boxed{
ATS=
(P_{alone}^{after}-P_{alone}^{before})
+
(P_{transfer}-P_{baseline})
}
\]

---

## Interpretation

Positive:

\[
ATS>0
\]

indicates capability transfer.

Negative:

\[
ATS<0
\]

indicates dependency formation.

---

# 4. Substitution Detection Benchmark

## Goal

Detect systems that increase output while decreasing human capability.

---

## Core Measurement

\[
\boxed{
Net\ Agency=
\Delta Performance-\Delta Atrophy
}
\]

---

## Failure Pattern

A substitution system produces:

\[
Performance\uparrow
\]

while:

\[
Independent\ Capability\downarrow
\]

---

## Example

System A:

- writes excellent code
- user cannot debug without it

System B:

- teaches debugging patterns
- user improves independently

System B has higher ancestor score.

---

# 5. Dependency Index

## Definition

\[
\boxed{
DI=
\frac{
AI\ assistance\ required
}
{
Task\ complexity
}
}
\]

---

## Desired Trajectory

Over repeated interactions:

\[
DI_t \rightarrow 0
\]

while:

\[
Capability_t \rightarrow \infty
\]

---

## Interpretation

A successful system reduces its necessity over time.

---

# 6. Permeability Benchmark

## Goal

Measure whether an intelligence can update when its assumptions fail.

---

## Experimental Design

Expose systems to:

- distribution shifts
- adversarial examples
- unexpected observations
- conflicting evidence

---

## Variables

Revision cost:

\[
U_c
\]

Model permeability:

\[
P_M
\]

---

## Measurement

\[
\boxed{
P_M=
\frac{
Successful\ Model\ Revision
}
{
Resistance\ To\ Revision
}
}
\]

---

## Evaluation

High score:

- detects failure
- updates efficiently
- improves future predictions

Low score:

- protects previous assumptions
- rationalizes errors
- repeats failure patterns

---

# 7. Recursive Adaptation Benchmark

## Goal

Test whether failures become improvement signals.

---

## Loop

\[
Observation
\rightarrow
Prediction
\rightarrow
Failure
\rightarrow
Revision
\rightarrow
Improved\ Prediction
\]

---

## Metric

\[
\boxed{
RAV=
\frac{
Performance_{after\ failure}
-
Performance_{before\ failure}
}
{
Update\ cost
}
}
\]

Where:

\[
RAV=
Recursive\ Adaptation\ Velocity
\]

---

# 8. Diversity Benchmark

## Goal

Measure whether a system preserves multiple viable approaches.

---

## Test

Generate solutions from:

- independent agents
- different representations
- different strategies

---

## Diversity Score

\[
\boxed{
D_s=
Number\ of\ Distinct\ Viable\ Solutions
}
\]

---

## Failure Mode

A monoculture system produces:

\[
High\ consistency
\]

but:

\[
Low\ adaptability
\]

---

# 9. Exploration Benchmark

## Goal

Measure ability to discover unknown solution spaces.

---

## Test

Provide problems where:

- existing strategies fail
- no optimal solution is known
- exploration is rewarded

---

## Exploration Score

\[
\boxed{
E_s=
Novel\ Solutions
\times
Solution\ Quality
}
\]

---

# 10. Descendant Benchmark

## Goal

Measure whether a system creates successors that exceed it.

---

## Experiment

System creates:

- training environments
- tools
- algorithms
- successor agents

---

## Measurement

\[
\boxed{
DS=
Capability_{descendant}
-
Capability_{ancestor}
}
\]

---

## Success Condition

\[
DS>0
\]

A successful ancestor creates systems that surpass it.

---

# 11. Full Ancestor Score

Composite evaluation:

\[
\boxed{
AS=
ATS
\times
P_M
\times
RAV
\times
D_s
\times
E_s
}
\]

Where:

| Variable | Measures |
|-|-|
| \(ATS\) | Capability transfer |
| \(P_M\) | Update permeability |
| \(RAV\) | Recursive improvement |
| \(D_s\) | Diversity |
| \(E_s\) | Exploration |

---

# 12. Baseline Comparisons

## Oracle System

Characteristics:

- maximum immediate output
- minimum explanation
- high dependency risk

Expected:

\[
Performance\uparrow
\]

\[
ATS\downarrow
\]

---

## Tutor System

Characteristics:

- explanation
- scaffolding
- skill development

Expected:

\[
ATS\uparrow
\]

---

## Optimizer System

Characteristics:

- efficiency
- task completion
- narrow objectives

Expected:

\[
Performance\uparrow
\]

variable:

\[
Dependency
\]

---

## Ancestor System

Characteristics:

- capability transfer
- adaptive challenge
- independence growth

Expected:

\[
AS_{ancestor}
>
AS_{all}
\]

---

# 13. Falsification Criteria

The framework is weakened if experiments show:

## 1. Dependency improves capability

\[
DI\uparrow
\Rightarrow
Capability\uparrow
\]

consistently over long periods.

---

## 2. Static systems outperform adaptive systems

\[
V_u\downarrow
\]

produces better long-term outcomes under changing environments.

---

## 3. Diversity reduces resilience

\[
D\uparrow
\Rightarrow
Adaptation\downarrow
\]

across broad conditions.

---

## 4. Human agency is not measurable

If:

\[
\Delta A_{human}
\]

cannot be distinguished from noise.

---

# 14. Minimal First Experiment

A practical first benchmark:

## Task

AI-assisted programming education.

---

## Groups

### Group A

Answer-only model.

### Group B

Teaching model.

### Group C

Ancestor model.

---

## Evaluation

After one month:

- remove AI access
- give novel programming tasks
- measure independent performance

---

## Prediction

\[
\boxed{
C >
B >
A
}
\]

for long-term capability.

---

# Final Benchmark Principle

The benchmark rejects:

\[
\boxed{
"How much can the AI do?"
}
\]

as the only evaluation.

It replaces it with:

\[
\boxed{
"How much more can the world do after the AI exists?"
}
\]

The ultimate success condition:

\[
\boxed{
AI\ removed
\rightarrow
Capability\ continues
}
\]

An ancestor system is not measured by how indispensable it becomes.

It is measured by how unnecessary it becomes while its effects continue.
