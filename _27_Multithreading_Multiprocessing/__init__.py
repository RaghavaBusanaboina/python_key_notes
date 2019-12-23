"""
There can only be one thread running at any given time in a python process:
--------------------------------------------------------------------------
1.Multiprocessing is parallelism. Multi-threading is concurrency.
2.Multiprocessing is for increasing speed. Multi-threading is for hiding latency(illusion).
3.Multiprocessing is best for computations(download file, different tasks).
     Multi-threading is best for IO(file handling, query DB, web pages loading).
4.If you have CPU heavy tasks, use multiprocessing with n_process = n_cores and never more. Never!
5.If you have IO heavy tasks, use multi-threading with n_threads = m * n_cores with m a number bigger
     than 1 that you can tweak on your own.
 Try many values and choose the one with the best speedup because there isn’t a general rule.
  For instance the default value of m in ThreadPoolExecutor is set to 5 [Source]
 which honestly feels quite random in my opinion.

"""