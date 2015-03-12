AdditionalLogger
===

**Summary**

Sometimes, in iOS/OSX, we need log message in some third-party library, but the library often doesn't provide support for logging. This tool can make source code for additional logger. After a simple configuration, you can log anything in the library.


**How To Use**

1. **Make source code**. use the `build.py` to make source code. For example, if you want to and additional logger to `FMDB` library, you can 
	
	`$ ./build.py --prefix=FMDB`
	
1. **Add source code to your project**. If no error occured, you can find the source code in `./generated` sub directory, as shown below. Then add the source code to your project.

	![](https://raw.githubusercontent.com/imoldman/AdditionalLogger/master/res/FMDBAdditionalLogger.png)
1. **Init the additional logger**. Put following code to `- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions` in your `AppDelegate`

	```
	#import "FMDBAdditionalLogger.h"
	```
	
    ```
	ALLoggerBlockType block = ^(int level, const char* fullpath, int line, const char* prefix, NSString* content) {	
        NSLog(@"%d [%s] %@ [%@:%d]", level, prefix, content, fullPath, line);
    };
    [FMDBAdditionalLogger setBlock:block];
    ```
1. **Log message to library**. Now you can log in FMDB!
 
	```
	#import "FMDBAdditionalLogger.h"
	```
 
    ```
    static int FMDBDatabaseBusyHandler(void *f, int count) {
	  ...    
      FMDBLOG_INFO(@"FMDBDatabaseBusyHandler result with 0, delta:%f, max:%f", delta, [self maxBusyRetryTimeInterval]);
	  return 0;
}
	```
	
**FAQ**

1. Q: Why I must have a prefix?
	
   A: OC has no namespace, so we need this prefix to indicate that it belongs to which module.


1. Q: Can I add the additional logger to multi library at the same time?

   A: Sure. Just don't forget init the additional logger in your `AppDelegate`.

