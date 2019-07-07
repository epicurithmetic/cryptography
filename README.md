### Cryptography

This repository is used as a place for me to store the code I write from my studies of cryptography. The two major sources for the ideas (protocols) I learn and problems I solve are (i) Cryptopals (https://cryptopals.com/), and (ii) the textbook *Understanding Cryptography* by Christof Paar.

At the moment this repository is *unedited/unoptimized stream-of-consciousness* code. 

#### What is in this repository
============================

This repository contains the code I have written to solve the problems on the Cryptopals website. For the most part I have tried to not use any packages/modules/libraries on top of the Python language. I try to implement all of the protocols and the mathematics needed for them myself; the primary goal is learning to code and learning cryptography, speed and efficiency are not the primary goal *at the moment*.

#### Cryptography Topics

The topics chosen for the cryptograpy algorithms are largely dictated by the cryptopals problem-set. I have code for the following protocols: 

- XOR Cipher:
  - Encrypt and decrypt
  - Break
Advanced Encryption Standard (AES):
  - Byte-substitution i.e. S-Box layer
  - Diffusion layer (still working on this)
  - Rijndael's key schedule (still working on this)
  - Inverting all of these layers for decryption (have not started on this)
  
A lot of the code for breaking encryption protocols require plaintext to be detected with out human-reading and input. In order to do this I have written some functions which measure the character frequency of a string and compare it to that of the expected frequency of written english. 

Taks for the near future include: 
1. Completing the basic AES implementation in Electronic Code Book
2. Learning other modes of operation for AES i.e. stream ciphers
3. Working on the cryptopals problems: 
    - Cryptopals Problem Set 1: Basics
      - [x] Problem 1 - Convert hex to base64
      - [x] Problem 2 - Fixed XOR
      - [x] Problem 3 - Single-byte XOR cipher
      - [x] Problem 4 - Detect single-character XOR
      - [x] Problem 5 - Implement repeating-key XOR
      - [x] Problem 6 - Break repeating-key XOR
      - [ ] Problem 7 - AES in ECB mode (Implement)
      - [x] Problem 8 Detect AES in ECB mode
     - Cryptopals Problem Sets 2-8

#### Number Theory Topics 

Number theory plays a large part in modern cryptography. Much of the code written in this repository is my way of figuring out how to implement the mathematics required to run the protocols. Topics include: 

- Elementary number theory:
  - Primes and factorisation
  - Euclidean Algorithm
  - Changing between base: binary, decimal, hex, and base64
- Finite field arithmetic:
  - Polynomial arithmetic over p = 2
  - Extensions of GF(2): multiplication and inverses
- Linear algebra over fintite fields:
  - Matrix arithmetic




