Custom Command and Control (C2) Framework

Overview

This project demonstrates a Command and Control (C2) framework used in cybersecurity to simulate how attackers communicate with compromised systems in a controlled environment.
It consists of a server and multiple agents that communicate using Python sockets, along with a simple dashboard for monitoring activity.

Architecture

server/ → Handles agent connections 
agent/ → Simulated client system 
dashboard/ → Web interface (Flask) 
utils/ → Communication & encryption helpers

Technologies Used

Python
Socket Programming
Flask
Threading

How to Run

Terminal 1 – Start the Server

cd c2-framework/server 
python handler.py

Terminal 2 – Start the Agent

cd c2-framework/agent 
python agent.py
