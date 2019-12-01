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

#### 0x00 ACC - Arithmetic Accumulator
#### 0x01 ARA - Arithmetic Register A
#### 0x02 ARB - Arithmetic Register B
#### 0x03 ARC - Arithmetic Register C
#### 0x04 ARD - Arithmetic Register D


get order of magnitude


### System Registers:
System registers are registers that serve to execute the program. They can also
be the target of computational operations.

#### 0x05 EXP - Execution Pointer
#### 0x06 SBP - Stack Base Pointer
#### 0x07 SHP - Stack Head Pointer


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

#### 0x00 BU a - Branch Unconditionally
Sets EXP to the value of a 
#### 0x01 BE a - Branch if Equal
Sets EXP to value of a if EF is 1
#### 0x02 BG a - Branch if Greater
Sets EXP to value of a if GF is 1
#### 0x03 BL a - Branch if Lesser
Sets EXP to value of a if LF is 1
#### 0x04 BZ a - Branch if Zero
Sets EXP to value of a if ZF is 1


### Arithmetic:
Arithmetic operations can occur only between registers.

#### 0x05 ADD dest a b - Add 
Add a to b, return int in dest
#### 0x06 SUB dest a b - Subtract 
Subtract a from b, return int in dest
#### 0x07 MUL dest a b - Multiply 
Multiply a by b, return int in dest
#### 0x08 DIV dest a b - Divide 
Divide a by b, return int in dest

#### 0x09 FADD dest a b - Floating Point Add
Add a to b, return float in dest
#### 0x0A FSUB dest a b - Floating Point Subtract
Subtract a to b, return float in dest 
#### 0x0B FMUL dest a b - Floating Point Multiply
Multiply a by b, return float in dest 
#### 0x0C FDIV dest a b - Floating Point Divide
Divide a by b, return float in dest 


### Bitwise:
These are various bitwise operators for encryption and logic.

#### 0x0D NOT dest a - Bitwise Not
Invert each bit in a and place it in dest register.
#### 0x0E AND dest a b Bitwise And
For each bit, if the bit in a and the bit in b are set high, set the bit in dest high.
#### 0x0F OR dest a b Bitwise Or
For each bit, if the bit in a or the bit in b are set high, set the bit in dest high.


### Special:
Special instructions can occur between registers and memory.

#### 0x10 COMP a b - Compare
Compare the contents of register a to the contents of register b
#### 0x11 LOAD a b - Load
Load from address b into register a
#### 0x12 PULL a b - Pull
Load from register b into address a
#### 0x13 PSH a - Push 
Push register or memory location to stack and increase SHP by 8
#### 0x14 POP a - Pop
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
Code pages are 1024 bytes in length


### Storage Management Unit
The SMU serves


## I/O

### Terminal Memory Map
Addresses 0x200 - 0x9D0 are part of the terminal memory map. Each address
represents a character on an 80x25 terminal display.

### Keyboard Memory Map
Addresses 0x000 - 0x200 are where keyboard input is placed.


## Syntactic Sugar:

### Comments
Comments are started using semicolons.

### Data Section
The start of each program is a data section designated with the `.data` 
directive. This section serves to declare named addresses and address ranges
(arrays). The section starts in memory at offset 0x1000

```
foo: r2A     ; foo is a range of 2A adresses. "foo" will reference offset 0 in that range.
bar: 100     ; bar is an address contianing the value 100
```


```
MAIN
	DATA
		val 10
	END DATA
	CODE
		LOAD val 0x200
	END CODE
END MAIN


```

To end the data section the `.end_data` directive is used.

### Code Section
The start of the code section is declared with the `.code` directive. Here code
is written. This section is ended with the `.end_code` directive.

### Functions:
Functions are syntactic sugar for jump statements and push/pop operations


```
.function A B
	.data
	
	.code
	
.end_function
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
.proc TEST
	.code
	ADD ACC ACC 1
	MOV testaddr ARD
	CMP ACC ARD
.end_proc
...
.data
testaddr 0x0F
.end_data
...
.code
.call TEST
.end_code

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
