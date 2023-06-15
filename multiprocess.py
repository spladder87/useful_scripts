from multiprocessing import Process
import ci_utils
import time

def build(project):
    basePath = "C:\dev\AMS_5x\\"
    artifactPath = "C:\dev\AMS_5x\log\\" 
    logData = ""
    logPath = f"{artifactPath}build_{project}.log"
    print(f"Building {project}")
    cmd = f"{basePath}work\\build.bat --proj={project} --clean"
    (ok, logData) = ci_utils.runCommand(cmd, logData)
    if ok == False:
        print(f"Failed!")

    # Save log to file
    ci_utils.writeFile(logData, logPath)
    print(f"finish {project}")
    #return logData

if __name__ == "__main__":  # confirms that the code is under main function
    start = time.time()
    print("hello")

    names = ['51', '54']
    procs = []

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=build, args=(name,))
        procs.append(proc)
        proc.start()
        time.sleep(5)

    # complete the processes
    for proc in procs:
        proc.join()
    end = time.time()
    print(f"time elapsed =",end - start)
