# PykdScript
Useful Pykd Script in Windbg debugging

## ListAllThreadAppDomainInfo.py
List All Thread AppDomain Information

- List all managed threads using !mex.mthreads;
- Split the result and save all clr!THREAD object to a list;
- Enumerate all items in the list and Dump AppDomain info of every clr!THREAD object;
- Save each result to ListAllThreadsAppDomainInfo.txt

[^Dependency extension]: [MEX](https://www.microsoft.com/en-us/download/details.aspx?id=53304)

## ListModuleReferenceInKernelDump.py
List All Module Reference in Kernel Dump

- List all processes using !process 0 0
- For each process , get the PEB information using !peb
- Save all result to ModuleReferenceInKernelDump.txt

## ListSocketGcroot.py
List All Socket Match With Fixed EndPoint Address

- Index all objects in dump using !netext.windex;
- Filter all System.Net.Sockets.Socket object matching with fixed EndPoint Address, e.g.192.168.0.100:8888 and save them to a list;
- For each object in list, we get the gcroot using command !gcroot
- Save all result to ListSocketGcroot.txt

[^Dependency extension]: [NETEXT](https://github.com/rodneyviana/netext)

## ListAllNonMicrosoftModule.py
List All Third-party Modules in Dump. We also can use command !mex.mods 

```
Usage:
    !mods [-q] [-l] [-k | -u] [-i] [-info] [-v] [-3] [-n] [-s <SortString>] [-r] [-net] [<Module Filter>] 
        -q                 : Don't display header
        -l                 : Display unloaded modules
        -k                 : Kernel modules only
        -u                 : User module only
        -i                 : Interesting modules only
        -info              : Displays FileInfo only
        -v                 : Verbose mode. Adds extra columns.
        -3                 : Try to limit output to only 3rd party modules.
        -n                 : Make the output note friendly.
        -s <SortString>    : Sorts by the specified column(s). Can specify more than one column at a time. (eg 'VBCT') (Default: B)
        -r                 : Rotate output
        -net               : Search .NET for missing modules
        Module Filter      : Regex Module filter

    !mods [-?] 
        -?|-help    : Display this help text

    Sort Options:
             m | M : Module name
             v | V : Version
             b | B : Base address
             c | C : Checksum
             t | T : Timestamp
             p | P : Path
             n | N : CLR
             f | F : Flags
    Uppercase is Ascending, lowercase is Descending

'Third Party' is determined by lack of 'Microsoft' in the Company field and lack of private symbols.

Current Owner: timhe
```

