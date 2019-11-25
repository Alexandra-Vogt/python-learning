# SECTIONS:
* Basic Architecture
* Registers and Flags
* Instructions
* Memory and Storage
* Syntactic Sugar


## Registers and Flags:
Registers and flags are what instructions mostly operate on.

### Arithmetic Registers:
Arithmetic registers serve to be the target of computational operations and the
execution of the code.

#### ACC - Arithmetic Accumulator
#### ARA - Arithmetic Register A
#### ARB - Arithmetic Register B
#### ARC - Arithmetic Register C
#### ARD - Arithmetic Register D


### System Registers:
System registers are registers that serve to execute the program. They can also
be the target of computational operations.

#### EXP - Execution Pointer
#### SBP - Stack Base Pointer
#### SHP - Stack Head Pointer


### Operation Flags:
Operation flags are set after an instruction is completed by the system.

#### ZF - Zero Flag
ZF = 1 if the previous instruction resulted in a zero being placed in ACC
#### NF - Negative Flag
NF = 1 if the previous instruction resulted in a negative value in ACC
#### OF - Overflow Flag
OF = 1 if the previous instruction caused arithmetic overflow


### Comparison Flags:
Comparison flags compare

#### EF - Equal Flag
EF = 1 if CMP a b where a = b
#### GF - Greater Flag
GF = 1 if CMP a b where a > b
#### LF - Lesser Flag
LF = 1 if CMP a b where a < b



## Instructions:
Instructions are stored as single bytes and executed.

### Branching:
Branching operations set EXP to the value of a.

#### BU a - Branch Unconditionally
Sets EXP to the value of a 
#### BE a - Branch if Equal
Sets EXP to value of a if EF is 1
#### BG a - Branch if Greater
Sets EXP to value of a if GF is 1
#### BL a - Branch if Lesser
Sets EXP to value of a if LF is 1
#### BZ a - Branch if Zero
Sets EXP to value of a if ZF is 1


### Arithmetic:
Arithmetic operations can occur only between registers.

#### ADD dest a b - Add 
Add a to b, return int in dest
#### SUB dest a b - Subtract 
Subtract a from b, return int in dest
#### MUL dest a b - Multiply 
Multiply a by b, return int in dest
#### DIV dest a b - Divide 
Divide a by b, return int in dest

#### FADD dest a b - Floating Point Add
Add a to b, return float in dest
#### FSUB dest a b - Floating Point Subtract
Subtract a to b, return float in dest 
#### FMUL dest a b - Floating Point Multiply
Multiply a by b, return float in dest 
#### FDIV dest a b - Floating Point Divide
Divide a by b, return float in dest 


### Special:
Special instructions can occur between registers and memory.

#### COMP a b - Compare
Compare the contents of register a to the contents of register b
#### LOAD a b - Load
Load from address b into register a
#### PSH a - Push 
Push register or memory location to stack and increase SHP by 8
#### POP a - Pop
Pop top value on stack, place it in register, and reduce SHP by 8

## Memory:
Memory is stored in 
```
Layout:
Program <----------------\
 \              |        |
  \-> TLB-->Main Memory  |
      |                  |
	  \->SMU             |
		   |             |
	        \-> Storage -/

Main Memory

```
### Memory Map Unit:
The memory map unit is a basic

Should the MMU determine that the requested page is located on disk, it makes


### Translation Lookaside Buffer:


### Code Pages:


### Storage Management Unit
The SMU serves



## Procedures and Functions:


### Functions:
Functions are syntactic sugar for jump statements and push/pop operations


```
FUNCTION A B
	.data
	
	.code
	
	
END FUNCTION
```

```
PUSH ACC      ; push everything onto stack
PUSH ARA 
PUSH ARB
PUSH ARC
PUSH ARD
PUSH EXP
PUSH SBP
PUSH SHP
PUSH SBP
LOAD SBP SHP ; set stack base pointer to stack head
PUSH A
PUSH B

...
SUB SBP, 8   ; reduce stack base pointer enough to get old stack base pointer
POP SBP      ; restore stack base pointer

POP SHP      ; restore everything else
POP HBP
POP EXP
POP ARD
POP ARC
POP ARB
POP ARA
POP ACC
```

### Procedures:
Procedures are syntactic sugar for jump statements and serve basically as mini
programs. They cannot access 

Procedures are declared in the following format:
```
PROC TEST
	.code
	ADD ACC ACC 1
	MOV testaddr ARD
	CMP ACC ARD
END PROC
...
.data
testaddr 0x0F
...
.code
CALL TEST

```
Which turns into:
```
.procedure
0x0001002C   ADD dest a b 
0x0001002D   MOV 
0x0001002E   CMP ACC
0x0001002F   JU 00020024
...
.data
0x00020046   0F
...
.code
0x00020073   JU 0001002B
```
