# Fundamentals of Natural Language Processing

Course material for **Fundamentals of NLP**, designed for:
- **M1 GAMMA** — Master 1 in Applied Mathematics
- **L2 LMAD Data Science** — Licence 2, Applied Mathematics for Data Science

This course introduces classical Natural Language Processing techniques that build the foundation for modern deep learning approaches. It assumes basic Python programming, machine learning concepts and linear algebra.

## Learning objectives

By the end of this course, students will be able to:

1. Define NLP and identify its core challenges (ambiguity, context, variability).
2. Recognize the major NLP tasks and their real-world applications.
3. Situate NLP within the broader Artificial Intelligence landscape.
4. Distinguish discriminative from generative modeling approaches.
5. Trace the historical evolution from rules to embeddings to LLMs.
6. Apply tokenization strategies and vector-space representations.
7. Compute and interpret evaluation metrics for both classification and generation tasks.

## Repository structure

```
.
├── Chapters/
│   ├── Chapter 1 - NLP Landscape/
│   └── Chapter 2 - Text Representation and Evaluation/
├── Notebooks/      (Python lab notebooks)
├── Slides/         (optional Beamer slides)
└── Full-course/    (unified PDF)
```

## Syllabus

### Chapter 1 — NLP Landscape
1. What is NLP? Core definition and fundamental challenges
2. Major NLP tasks and applications
3. NLP within the AI ecosystem
4. Discriminative vs. generative models
5. Historical evolution: from rules to embeddings to LLMs

### Chapter 2 — Text Representation and Evaluation
1. Tokenization fundamentals
2. Vector space models: sparse representations (BoW, TF-IDF)
3. Dense distributed representations (Word2Vec, GloVe, FastText)
4. Semantic similarity measures
5. Evaluation metrics: classification (Precision, Recall, F1) and generation (Perplexity, BLEU, ROUGE)

## Compilation

Each chapter compiles independently:

```bash
cd "Chapters/Chapter 1 - NLP Landscape"
pdflatex chapter1.tex
```

The unified course PDF is built from `Full-course/main.tex`:

```bash
cd Full-course
pdflatex main.tex
pdflatex main.tex   # second pass for ToC
```

## Author

Aymen Ben Brik
