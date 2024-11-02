# Requiem: Pythonic Common Games™

Project Release V1.0 [(Install it now!)](./intro/installation.md)

A Python library for creating simple common games, and displaying them on the web.

---

**Requiem** provides you the tools required to easily make simple common games, such as chess, 2048, number guessing, sissors paper stone, ect... all within Python. The vanilla way of making games in Python is difficult, so why not just use a libary to simplify it?

Check it out with a simple example:

``` python
# An example for Python Chess
import requiem

board = chess.Board()

board.legal_moves  
<LegalMoveGenerator at ... (Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, ...)>
chess.Move.from_uci("a8a1") in board.legal_moves
False

board.push_san("e4")
Move.from_uci('e2e4')
board.push_san("e5")
Move.from_uci('e7e5')
board.push_san("Qh5")
Move.from_uci('d1h5')
board.push_san("Nc6")
Move.from_uci('b8c6')
board.push_san("Bc4")
Move.from_uci('f1c4')
board.push_san("Nf6")
Move.from_uci('g8f6')
board.push_san("Qxf7")
Move.from_uci('h5f7')

board.is_checkmate()
True

board
Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')
```

## Core Features:

::::{grid} 1 1 2 2
:::{grid-item-card} {octicon}`archive` Game Support
Supports multiple games, and if requried, you can declare your own components!
:::
:::{grid-item-card}  {octicon}`git-branch` Workflow Integreation
Goes smoothly with GitHub workflows, CI/CD, and pipelines.
:::
:::{grid-item-card} {octicon}`cache` Batteries Included
- Includes some web framework, so you can run your game on a local server.
:::
:::{grid-item-card} {octicon}`codespaces` Deploy Anywhere
Host your Project anywhere, thanks to said web framework.
:::
::::

## Project Implementations

## Site Navigation

You can use this section to navigate these documents. The first section covers the basics of Requiem, from installation to application.

### Game Guides

Guides for creating your Python game are here, from extending your application to creating multiple games in the same project.

```{toctree}
intro/installation
intro/quickstart
```

### Framework Guides

```{toctree}
framework/web-application.md
```