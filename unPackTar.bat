ECHO off
for %%a in (*.tar) do (
    echo %%a    
    tar -xf %%a
    del %%a
)