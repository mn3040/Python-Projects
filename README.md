# Python Implementations

This repository contains several implementations of popular games and data structures, including Blackjack, Tic-Tac-Toe, Guessing Game, Binary Search Tree Map.

## Blackjack

A simple implementation of the Blackjack card game in Python. The game includes functionality for dealing cards to both the player and the dealer, determining the value of hands, and deciding the winner.

### Features
- Dealing cards to the player and the dealer
- Calculating the value of each hand
- Determining the winner

## Tic-Tac-Toe

A classic implementation of the Tic-Tac-Toe game in Python. Players take turns marking a space in a 3x3 grid, aiming to be the first to get three marks in a row.

### Features
- Player input for marking the grid
- Displaying the current state of the board
- Determining the winner or if there is a draw


## Guessing Game

A simple word guessing game implemented in Python. Players guess letters in a word, with a limited number of incorrect guesses allowed.

### Features
- Reading a list of words from a file
- Allowing the player to guess letters
- Displaying the current state of the word and missed guesses
- Determining if the player has won or lost

# Binary Search Tree Map Implementation

This project implements a binary search tree (BST) map in Python, providing an efficient way to store and retrieve key-value pairs. The BST map supports standard map operations, including insertion, deletion, and lookup, with additional functionality for tree traversal and finding the ith smallest element.

## Features

- **Insertion:** Add a key-value pair to the BST.
- **Deletion:** Remove a key-value pair from the BST.
- **Lookup:** Retrieve the value associated with a given key.
- **Traversal:** Perform an in-order traversal of the BST.
- **Find ith Smallest:** Find the ith smallest key in the BST.

## Class Structure

### `BinarySearchTreeMap`
This is the main class representing the binary search tree map.

#### Inner Classes
- **`Item`:** Represents a key-value pair.
- **`Node`:** Represents a node in the BST, containing an `Item` and pointers to parent, left, and right child nodes.

### Methods

- **`__init__()`:** Initializes an empty BST map.
- **`__len__()`:** Returns the number of elements in the BST.
- **`is_empty()`:** Checks if the BST is empty.
- **`__getitem__(key)`:** Retrieves the value associated with the given key.
- **`find(key)`:** Finds the node with the given key.
- **`__setitem__(key, value)`:** Sets the value for the given key. If the key does not exist, it inserts a new key-value pair.
- **`insert(key, value)`:** Inserts a new key-value pair into the BST.
- **`__delitem__(key)`:** Deletes the key-value pair with the given key.
- **`delete(node_to_delete)`:** Deletes the specified node from the BST.
- **`subtree_max(curr_root)`:** Finds the node with the maximum key in the given subtree.
- **`inorder()`:** Performs an in-order traversal of the BST.
- **`__iter__()`:** Returns an iterator for the BST keys.
- **`get_ith_smallest(i)`:** Finds the ith smallest key in the BST.
