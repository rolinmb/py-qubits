I tried implementing Qubits before and had a somewhat comparable simulation to that of Microsoft's Q# SDK. (see my qsharp & qubits repos; ignore any Quantum Register implementations)

The main idea behind this was seeding the random right before every "observation" of the singleton qubit. That sounded more like how nature behaves in my mind. It would just require more CPU cycles to simulate a singleton qubit this way (idk how python random works someone fact check me).

Run src/main.py from root:
    -> python src/main.py

If you run the program as it currently is, it will simulate N_ITERS unique 50%/50% event and a 66.66%/33.33% outcome events. (aka every time you run it; because of how random is always re-seeded; there will be a new number of zeros and ones in each simulation)i