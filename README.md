# CNEP Banque - FLOW

## Overview

This repository contains the FLOW application, developed during an internship at CNEP-Banque (Caisse Nationale d’Epargne et de Prévoyance), an Algerian financial institution focusing on household savings, housing finance through mortgages, and financing companies involved in the building sector.

### Internship Theme: Information System and Database Management

## Problem Statement

CNEP Banque, particularly the Tizi Ouzou branch, faced challenges due to decentralized data management across its extensive network of branches. Each branch stored its own data, leading to discrepancies and inconsistencies among branches.

The inconsistency in financial data hindered strategic decision-making, performance evaluation, and the delivery of high-quality services to clients. The lack of coherent data posed difficulties in consolidating and accurately analyzing information.

## Client Requirements

The client, CNEP Banque Tizi Ouzou, required a client-server application to address the issue of varied data across branches. The goal was to establish centralized access to the database, ensuring each branch accessed the same financial information.

By centralizing the database, the project aimed to harmonize financial information across all branches, facilitating comprehensive analysis and decision-making. This centralized approach aimed to eliminate inconsistencies, enhancing decision-making and overall bank operation management.

## FLOW Architecture

The "FLOW" application is structured based on the client-server model, where both entities collaborate to deliver the application's functionalities.

### Components:

- **Server-Side (MOVE Directory):**
  - Contains server-side files developed using the Django framework for efficient data management with MySQL.

- **Client-Side (UI Directory):**
  - Holds client-side files for the user interface, developed using PyQt5 to create an intuitive and user-friendly experience.

### Interaction Flow:

- **User Interaction:**
  - Users interact with the user interface, initiating requests that are transmitted to the server through the HTTP protocol.

- **Server Processing:**
  - The server processes these requests, executing necessary operations on the database to fulfill user actions.

### Benefits of Client-Server Architecture:

The client-server architecture adopted in "FLOW" ensures a clear separation of responsibilities between the client (user interface) and the server (business logic and data management). This design choice offers:

- **Efficient Scalability:** Allows for scalable growth to accommodate increasing user demands.
- **Optimized Request Handling:** Enables streamlined management of requests and operations.
- **Creation of a Robust Application:** Facilitates the development of a powerful, secure, and user-friendly application that efficiently meets user needs.

## Technologies Used

The client (CNEP Banque) provided flexibility in choosing development languages and technologies. Leveraging familiarity with Python and its versatile ecosystem, I selected Python due to its open-source nature, versatility, and robustness.

- **Front-End (Client-side):** 
  - Utilized the Python Qt library for the application's client-side development.

- **Back-End (Server-side):** 
  - Employed the Django framework to build the server-side functionality.

- **Database Management:** 
  - Implemented a relational database management system (RDBMS) using MySQL for efficient data management.

## Application Overview

### FLOW - Visualizing Transactions

The application named "FLOW" and that's for emphasizing its core purpose of visualizing and tracking various transaction flows within CNEP Banque - Tizi Ouzou.

### Objectives

**FLOW** has been meticulously created to address the bank's needs in monitoring and managing financial transactions. It presents an intuitive and user-friendly interface tailored to empower users in visualizing and analyzing transaction flows seamlessly.

### Key Features

- **Efficient Transaction Tracking:**
  - Users can efficiently consult and track transaction flows within the bank.
- **Comprehensive Transaction Insights:**
  - Detailed information, including amounts, dates, and involved accounts, is readily accessible.
- **Search Capabilities:**
  - Enables users to conduct specific transaction searches for comprehensive analysis.

### Functionality

The application empowers users to explore both historical and current transactions, providing a platform to delve into transactional details and perform necessary analyses.
