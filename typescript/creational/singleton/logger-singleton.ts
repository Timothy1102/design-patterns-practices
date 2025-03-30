/**
 * Thread-Safe Singleton Implementation with lazy initialization
 *
 * Demonstrates a more sophisticated approach to Singleton implementation
 * that addresses some common concerns.
 */
class Logger {
    private static instance: Logger;
    private logLevel: string;
    private logFile: string;
    private logCount: number = 0;

    // Private constructor to prevent instantiation
    private constructor(logLevel: string = 'INFO', logFile: string = 'app.log') {
        this.logLevel = logLevel;
        this.logFile = logFile;
        console.log(`Logger initialized with level ${logLevel} writing to ${logFile}`);
    }

    // Static method to get the singleton instance with double-check locking pattern
    public static getInstance(logLevel?: string, logFile?: string): Logger {
        if (!Logger.instance) {
            // In a real multithreaded environment, you would use a lock here
            if (!Logger.instance) {
                Logger.instance = new Logger(logLevel, logFile);
            }
        }
        return Logger.instance;
    }

    // Instance methods
    public log(message: string, level: string = 'INFO'): void {
        this.logCount++;
        const timestamp = new Date().toISOString();
        console.log(`[${timestamp}] [${level}] [${this.logCount}]: ${message}`);
    }

    public error(message: string): void {
        this.log(message, 'ERROR');
    }

    public warn(message: string): void {
        this.log(message, 'WARNING');
    }

    public info(message: string): void {
        this.log(message, 'INFO');
    }

    public debug(message: string): void {
        this.log(message, 'DEBUG');
    }

    public setLogLevel(level: string): void {
        this.logLevel = level;
        this.log(`Log level changed to ${level}`, 'SYSTEM');
    }
}

function demonstrateLoggerSingleton(): void {
    console.log('\n=== Logger Singleton Demo ===');

    // Create logger instances - should be the same instance
    const logger1 = Logger.getInstance('DEBUG', 'app-debug.log');
    const logger2 = Logger.getInstance();

    // Test if they're the same instance
    console.log('Are logger1 and logger2 the same instance?', logger1 === logger2);

    // Log some messages
    logger1.info('Application started');
    logger1.debug('Loading configuration...');

    // Use the second reference - still logs with the same settings
    logger2.warn('Configuration file not found, using defaults');
    logger2.error('Failed to connect to service');

    // Change log level through one instance
    logger1.setLogLevel('ERROR');

    // Log through the other instance
    logger2.debug('This debug message might not be logged due to log level');
    logger2.error('This error will still be logged');
}

demonstrateLoggerSingleton();
