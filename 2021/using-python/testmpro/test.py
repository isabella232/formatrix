import multiprocessing
import time
import one

myone = one.One()

if __name__ == '__main__':
  # Start foo as a process
  man = multiprocessing.Manager()
  testlist = man.list()
  p = multiprocessing.Process(target=myone.run, name="Foo", args=(4,testlist,))
  p.start()

  # Wait 10 seconds for foo
  # time.sleep(10)

  p.join(5)

  # If thread is active
  if p.is_alive():
    print( "foo is running... let's kill it...")

    # Terminate foo
    p.terminate()
    p.join()
  else:
    print("completed before 5 sec")
  print(testlist)