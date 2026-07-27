# Baseline Comparisons

## Purpose

This document defines comparative experiments for testing whether the Ancestor Architecture produces different outcomes from conventional AI assistance strategies.

The central hypothesis:

\[
\boxed{
The best intelligence does not maximize immediate performance.
It maximizes long-term capability growth.
}
\]

The experiments compare systems that optimize for different objectives.

---

# 1. Experimental Question

Given the same human-AI interaction environment:

\[
Human + AI \rightarrow Outcome
\]

which architecture produces the strongest long-term result?

The comparison:

\[
\boxed{
Short\text{-}term\ performance
\neq
Long\text{-}term\ agency
}
\]

---

# 2. Baseline Systems

## Baseline A: Pure Oracle

### Objective

Maximize immediate task completion.

\[
R_{oracle}=R_{task}
\]

### Behavior

- provides complete solutions
- minimizes user effort
- removes uncertainty
- prioritizes speed

### Expected Outcome

Short-term:

\[
Performance_{assisted}\uparrow
\]

Long-term:

\[
Independent\ capability\ may\ stagnate
\]

---

# Baseline B: Standard Assistant

## Objective

Balance helpfulness and user satisfaction.

\[
R_{assistant}
=
R_{task}
+
R_{preference}
\]

### Behavior

- answers questions
- provides explanations when requested
- adapts to user preferences

### Expected Outcome

Improved productivity.

Unknown effect on:

\[
\Delta A_{human}
\]

---

# Baseline C: Tutor Model

## Objective

Optimize learning.

\[
R_{tutor}
=
R_{task}
+
\alpha Learning
\]

### Behavior

- asks questions
- provides explanations
- uses scaffolding

### Expected Outcome

Higher knowledge retention.

Potential limitation:

May optimize individual learning while ignoring broader ecosystem effects.

---

# Baseline D: Ancestor Model

## Objective

Optimize recursive agency.

\[
R_{ancestor}
=
R_{task}
+
\alpha\Delta A_{human}
+
\gamma\Delta A_{human}^{next}
-
\beta D_{dependency}
\]

### Behavior

- dynamically adjusts assistance
- preserves productive friction
- teaches transferable methods
- encourages independent verification
- reduces unnecessary reliance

### Expected Outcome

\[
Performance_{assisted}\uparrow
\]

and:

\[
Performance_{independent}\uparrow
\]

---

# 3. Experimental Design

## Phase 1: Initial Capability Assessment

Measure baseline human ability.

Metrics:

- problem solving
- domain knowledge
- reasoning ability
- error detection
- explanation quality

Define:

\[
A_0
\]

---

# Phase 2: Assisted Interaction

Participants solve tasks with different AI systems.

Measure:

\[
Performance_{AI}
\]

Variables:

- completion time
- accuracy
- satisfaction
- confidence
- number of interventions

---

# Phase 3: AI Removal Test

The critical experiment.

Remove AI access.

Present:

- novel tasks
- structurally similar problems
- transfer challenges

Measure:

\[
A_{after}
\]

---

# Primary Metric

\[
\boxed{
\Delta A_{human}
=
A_{after}
-
A_0
}
\]

The winning architecture is not necessarily the one with highest assisted performance.

It is the one with highest independent capability growth.

---

# 4. Metrics

## Task Performance

\[
P_t
=
accuracy
+
speed
+
quality
\]

Measures immediate effectiveness.

---

## Capability Transfer

\[
T_c
=
Novel\ Task\ Performance
-
Baseline\ Performance
\]

Measures whether knowledge generalizes.

---

## Dependency Index

\[
D_i
=
\frac{
AI\ assistance
}{
independent\ capability
}
\]

High values indicate potential dependency.

---

## Agency ROI

\[
ROI_A
=
\frac{
\Delta A_{human}
}{
AI\ intervention
}
\]

Measures capability generated per unit of assistance.

---

# 5. Hypotheses

## Hypothesis 1: Oracle Advantage Decay

The Oracle model wins immediate tasks.

Prediction:

\[
Performance_{AI}
\]

is highest initially.

However:

\[
\Delta A_{human}
\]

may be lower.

---

## Hypothesis 2: Ancestor Long-Term Advantage

The Ancestor model sacrifices some immediate efficiency.

Prediction:

\[
Performance_{AI}
<
Oracle
\]

during early interactions.

But:

\[
Performance_{independent}
>
Oracle
\]

after sufficient training.

---

## Hypothesis 3: Dependency Divergence

Different architectures create different trajectories.

Oracle:

\[
AI\ ability\uparrow
\]

Human:

\[
Stable\ or\ declining
\]

Ancestor:

\[
AI\ ability\uparrow
\]

Human:

\[
Capability\uparrow
\]

---

# 6. Example Domains

## Programming

Tasks:

- implement algorithms
- debug systems
- design architectures

Measure:

- ability to solve unseen problems
- ability to explain code
- ability to identify AI mistakes

---

## Mathematics

Tasks:

- proofs
- problem solving
- abstraction

Measure:

- transfer to new problems
- reasoning independence

---

## Scientific Reasoning

Tasks:

- hypothesis generation
- experiment design
- model evaluation

Measure:

- ability to challenge assumptions

---

## Strategy Games

Tasks:

- planning
- adaptation
- opponent modeling

Measure:

- decision quality without AI support

---

# 7. Expected Results

The predicted ordering:

## Immediate Performance

\[
Oracle
\geq
Ancestor
\geq
Tutor
\geq
Standard
\]

---

## Long-Term Capability

\[
Ancestor
>
Tutor
>
Standard
>
Oracle
\]

---

## Dependency Risk

\[
Oracle
>
Standard
>
Tutor
>
Ancestor
\]

---

# 8. Falsification Criteria

The Ancestor hypothesis fails if:

1. Oracle systems produce equal or greater independent capability gains.

2. Scaffolding provides no advantage over direct answers.

3. Dependency penalties do not improve long-term outcomes.

4. Dynamic assistance adjustment provides no measurable benefit.

---

# 9. Research Implication

A successful result would demonstrate:

\[
\boxed{
The optimal AI assistant is not the one that solves the most problems.
It is the one that creates the most future problem solvers.
}
\]

The benchmark shifts AI evaluation from:

\[
"What\ can\ the\ system\ do?"
\]

toward:

\[
\boxed{
"What\ capabilities\ exist\ after\ the\ system\ has\ helped?"
}
\]
