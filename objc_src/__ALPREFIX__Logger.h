//
//  __ALPREFIX__Logger.h, create by TODO
//

#import <Foundation/Foundation.h>

#ifndef ALLOGGERLEVELDEFINED
#define ALLOGGERLEVELDEFINED 1
#define ALLOGGERLEVEL_VERBOSE 1
#define ALLOGGERLEVEL_DEBUG 2
#define ALLOGGERLEVEL_INFO 3
#define ALLOGGERLEVEL_WARN 4
#define ALLOGGERLEVEL_ERROR 5
#endif

#define __ALPREFIX_UPPER__LOG(level, content, ...) do { \
    [__ALPREFIX__Logger logWithLevel:level file:__FILE__ line:__LINE__ prefix:"__ALPREFIX__" log:(content), ##__VA_ARGS__]; \
} while(0)

#define __ALPREFIX_UPPER__LOG_VERBOSE(content, ...) __ALPREFIX_UPPER__LOG(ALLOGGERLEVEL_VERBOSE, content, ##__VA_ARGS__)
#define __ALPREFIX_UPPER__LOG_DBUG(content, ...) __ALPREFIX_UPPER__LOG(ALLOGGERLEVEL_DEBUG, content, ##__VA_ARGS__)
#define __ALPREFIX_UPPER__LOG_INFO(content, ...) __ALPREFIX_UPPER__LOG(ALLOGGERLEVEL_INFO, content, ##__VA_ARGS__)
#define __ALPREFIX_UPPER__LOG_WARN(content, ...) __ALPREFIX_UPPER__LOG(ALLOGGERLEVEL_WARN, content, ##__VA_ARGS__)
#define __ALPREFIX_UPPER__LOG_ERROR(content, ...) __ALPREFIX_UPPER__LOG(ALLOGGERLEVEL_ERROR, content, ##__VA_ARGS__)


#ifndef ALLOGGERBLOCKTYPEDEFINED
#define ALLOGGERBLOCKTYPEDEFINED 1
typedef void(^ALLoggerBlockType)(int level, const char* fullpath, int line, const char* prefix, NSString* content);
#endif


@interface __ALPREFIX__Logger : NSObject
+ (void)setBlock:(ALLoggerBlockType)block;
+ (ALLoggerBlockType)block;

+ (void)logWithLevel:(int)level file:(const char *)fullpath line:(int)line prefix:(const char*)prefix log:(NSString *)content, ...;
@end
