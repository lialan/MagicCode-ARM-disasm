0. apply the patch to your MagicCode repo.
```
git apply annotate.patch
```
1. download darm into this folder:
```
git clone git://github.com/jbremer/darm.git
```
2. compile darm:
```
cd darm; make;
```
3. call get_nm.py to populate the dynamic relocation symbols to /tmp/sopickle
```
get_nm.py sofilename1.so sofilename2.so ...
```
4. run annotate.py:
```
annotate logcat_file.txt
```

Step 4 will generate the annotated file at:
```
/tmp/annotated_logcat.txt
```

The idea behind this is very simple: let MagicCode to print out the ARM instruction encoding, 
and then grep it and replace it with ARM disassembler along with the offset to the function.

Notes:
This script uses nm for arm, you can change the actual nm command in get_nm.py
```
ARM_NM_NAME = 'arm-none-eabi-nm'
```
