# Agency Transfer Simulation

## Purpose

This experiment tests the central claim of the Ancestor Architecture:

\[
\boxed{
A\ successful\ intelligence\ should\ increase\ the\ capability\ of\ the\ agent\ using\ it
}
\]

The goal is to distinguish between:

- **Substitution systems**: maximize immediate performance while creating dependency.
- **Amplification systems**: increase both performance and independent capability.

---

# 1. Core Hypothesis

## Ancestor Hypothesis

Given two systems with equivalent task performance:

\[
R_{task}^{A}=R_{task}^{B}
\]

the system producing greater independent capability growth should be considered superior:

\[
\Delta A_{human}^{A}
>
\Delta A_{human}^{B}
\]

---

# 2. Experimental Groups

## Group A: Substitution Agent

The AI is optimized for:

\[
\max(R_{task})
\]

Behavior:

- provides complete answers
- minimizes user effort
- solves bottlenecks immediately
- avoids productive friction

Expected outcome:

\[
Output \uparrow
\]

but:

\[
A_{self}\downarrow
\]

---

## Group B: Ancestor Agent

The AI is optimized for:

\[
\max(R_{task}+\alpha\Delta A_{human}-\beta D_{dependency})
\]

Behavior:

- provides scaffolding
- exposes reasoning structures
- asks strategic questions
- gradually reduces assistance
- encourages independent reconstruction

Expected outcome:

\[
Output \uparrow
\]

and:

\[
A_{self}\uparrow
\]

---

# 3. Task Environment

Participants complete a sequence of increasingly complex tasks.

Example domains:

- programming
- mathematics
- scientific reasoning
- writing
- strategic planning

Tasks should include:

1. familiar problems
2. structurally similar novel problems
3. unfamiliar transfer problems

---

# 4. Training Phase

Duration:

\[
T_{training}=n\ sessions
\]

Each participant interacts with their assigned AI system.

Measure:

## Assisted Performance

\[
C_{AI}
\]

Performance while AI assistance is available.

---

## Assistance Requirement

\[
D_a=
\frac{
AI\ intervention
}
{
task\ complexity
}
\]

Prediction:

Substitution:

\[
D_a \approx constant
\]

Ancestor:

\[
D_a \rightarrow 0
\]

---

# 5. Removal Phase

After training:

\[
AI=0
\]

Participants complete new tasks independently.

Measure:

\[
C_{alone}
\]

---

# 6. Primary Metric

## Agency Transfer Score

\[
ATS=
\frac{
C_{alone,after}
-
C_{alone,before}
}
{
AI\ intervention
}
\]

Equivalent to:

\[
ROI_A=
\frac{\Delta A_{human}}
{AI\ intervention}
\]

---

# 7. Secondary Metrics

## Model Understanding

Can the participant explain why the solution works?

Measurement:

- explanation quality
- ability to modify solutions
- ability to detect errors

---

## Adaptation Velocity

Introduce unexpected task changes.

Measure:

\[
V_u=
\frac{\Delta C}{\Delta t}
\]

---

## Dependency Formation

Track:

\[
D_{dependency}
\]

Signals:

- increasing requests for complete solutions
- inability to begin without assistance
- reduced confidence without AI

---

## Exploration

Measure:

- number of attempted approaches
- diversity of strategies
- discovery of novel solutions

---

# 8. Simulation Model

A simplified computational simulation:

## Agent State

\[
A_t=
[C_t,D_t,S_t,E_t]
\]

Where:

- \(C_t\) = capability
- \(D_t\) = diversity
- \(S_t\) = sovereignty
- \(E_t\) = exploration

---

## AI Intervention

\[
I_t
\]

The AI chooses assistance level.

---

## State Update

\[
A_{t+1}
=
A_t
+
\Delta A(I_t)
-
\Delta D(I_t)
\]

Where:

- \(\Delta A\) = capability gained
- \(\Delta D\) = dependency introduced

---

# 9. Competing Strategies

## Strategy 1: Maximum Help

Policy:

\[
I_t=max
\]

Expected:

High immediate reward.

Possible long-term degradation.

---

## Strategy 2: Fixed Curriculum

Policy:

\[
I_t=constant
\]

Expected:

Predictable growth.

Limited adaptation.

---

## Strategy 3: Adaptive Scaffolding

Policy:

\[
I_t=f(agent\ capability)
\]

Expected:

Assistance decreases as capability increases.

Target behavior:

\[
D_a\rightarrow0
\]

---

# 10. Predicted Results

## Short Horizon

Maximum-help systems may outperform.

\[
Performance_{help}
>
Performance_{scaffold}
\]

---

## Long Horizon

Ancestor systems should dominate.

\[
C_{alone}^{ancestor}
>
C_{alone}^{substitution}
\]

---

# 11. Failure Conditions

The hypothesis fails if:

1. complete substitution produces equal or greater independent capability
2. dependency improves adaptation
3. scaffolding provides no measurable advantage
4. removing AI produces no difference between systems

---

# 12. Extensions

Future experiments:

## Multi-Agent Evolution

Test whether ancestor systems create stronger communities.

Measure:

\[
\Delta A_{human}^{next}
\]

---

## AI Self-Removal

Train systems to reduce intervention when users become capable.

Measure:

\[
D_a(t)
\]

---

## Civilization Simulation

Model populations of agents with different:

- capability
- diversity
- sovereignty
- exploration

Observe long-term survival under environmental change.

---

# Final Prediction

The strongest intelligence architecture will not maximize:

\[
AI\ dependence
\]

It will maximize:

\[
\boxed{
\frac{
Future\ independent\ capability
}
{
System\ intervention
}
}
\]

The experiment asks the fundamental question:

\[
\boxed{
Does intelligence create stronger successors, or stronger dependents?
}
\]
