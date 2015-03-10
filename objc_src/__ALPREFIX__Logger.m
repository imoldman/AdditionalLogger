//
//  __ALPREFIX__Logger.m, create by TODO
//

#import "__ALPREFIX__Logger.h"

@interface __ALPREFIX__Logger ()
@property (nonatomic, copy) ALLoggerBlockType logBlock;
@end

@implementation __ALPREFIX__Logger

+ (instancetype)sharedInstance
{
    static __ALPREFIX__Logger* instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc] init];
    });
    return instance;
}

+ (void)setBlock:(ALLoggerBlockType)block
{
    [[__ALPREFIX__Logger sharedInstance] setLogBlock:block];
}

+ (ALLoggerBlockType)block
{
    return [[__ALPREFIX__Logger sharedInstance] logBlock];
}

+ (void)logWithLevel:(int)level file:(const char *)fullpath line:(int)line prefix:(const char*)prefix log:(NSString *)log, ...
{
    ALLoggerBlockType block = [self block];
    if (block != nil) {
        va_list vl;
        va_start(vl, log);
        NSString* content = [[NSString alloc] initWithFormat:log arguments:vl];
        va_end(vl);
        block(level, fullpath, line, prefix, content);
    }
}

@end