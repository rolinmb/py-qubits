I tried implementing Qubits before and had a somewhat comparable simulation to that of Microsoft's Q# SDK. (see my qsharp & qubits repos; ignore any Quantum Register implementations)

The main idea behind this was seeding the random right before every "observation" of the singleton qubit. That sounded more like how nature behaves in my mind. It would just require more CPU cycles to simulate a singleton qubit this way (idk how python random works someone fact check me).

NO REQUIREMENTS! Run src/main.py from root:
    -> python src/main.py

If you run the program as it currently is, it will simulate N_ITERS unique events. (aka every time you run it random is re-seeded)

TODO:
    -> Abstract Qubit and Qutrit to an n-outcome Quantum logit / event; where the sum of probabiltities of each N outcome states still sums to 1 as defined in a Qubit and Qutrit

    -> Try and implement simple Quantum Register with qubits; i.e. simulate how two qubits could be entangled and thus be collapsed into 4 possible observed outcome states, some of which may not be observable given how the qubits are entangled to make a register. My understanding breaks down here. A quantum register cannot consist of singleton qubits as the regiser's sum of probabilties must equal 1; not the individual qubit or qutrit or n-outcome quantum logic unit encodes.

    -> A true quantum register could be comprised of the single outcome events; binary events, tertiary events,... any n-outcome event all together to describe the true behavior of a quantum system.

    -> Try to implement Quantum Registers as a type of matrix of complex numbers; that way one can abstract the quantum register away and leverage GPU's or beter arithmetic processors than CPUs to more efficiently collapse and measure quantum systems.