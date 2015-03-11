//
//  __ALPREFIX__AdditionalLogger.m, create by https://github.com/imoldman/AdditionalLogger
//

#import "__ALPREFIX__AdditionalLogger.h"

@interface __ALPREFIX__AdditionalLogger ()
@property (nonatomic, copy) ALLoggerBlockType logBlock;
@end

@implementation __ALPREFIX__AdditionalLogger

+ (instancetype)sharedInstance
{
    static __ALPREFIX__AdditionalLogger* instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc] init];
    });
    return instance;
}

+ (void)setBlock:(ALLoggerBlockType)block
{
    [[self sharedInstance] setLogBlock:block];
}

+ (ALLoggerBlockType)block
{
    return [[self sharedInstance] logBlock];
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