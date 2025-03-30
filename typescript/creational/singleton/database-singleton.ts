/**
 * Basic Singleton Pattern Implementation
 *
 * This implementation ensures that only one instance of DatabaseConnection
 * can exist at any time.
 */
class DatabaseConnection {
    private static instance: DatabaseConnection;
    private connectionString: string;
    private isConnected: boolean = false;

    // Private constructor prevents instantiation from outside
    private constructor(connectionString: string) {
        this.connectionString = connectionString;
        console.log(`DatabaseConnection instance created with connection string: ${connectionString}`);
    }

    // Static method to access the singleton instance
    public static getInstance(connectionString: string = 'default-connection-string'): DatabaseConnection {
        if (!DatabaseConnection.instance) {
            DatabaseConnection.instance = new DatabaseConnection(connectionString);
        }
        return DatabaseConnection.instance;
    }

    // Instance methods
    public connect(): void {
        if (this.isConnected) {
            console.log('Already connected to the database');
            return;
        }

        console.log(`Connecting to database with ${this.connectionString}...`);
        // Simulate connection process
        this.isConnected = true;
        console.log('Database connection established successfully');
    }

    public disconnect(): void {
        if (!this.isConnected) {
            console.log('Not connected to the database');
            return;
        }

        console.log('Disconnecting from database...');
        // Simulate disconnection process
        this.isConnected = false;
        console.log('Database connection closed');
    }

    public executeQuery(query: string): any[] {
        if (!this.isConnected) {
            throw new Error('Cannot execute query. Not connected to the database.');
        }

        console.log(`Executing query: ${query}`);
        // Simulate query execution
        return [{id: 1, name: 'Result 1'}, {id: 2, name: 'Result 2'}];
    }

    // Method to get connection status (useful for testing)
    public getConnectionStatus(): boolean {
        return this.isConnected;
    }
}

// Example usage
function demonstrateDatabaseSingleton(): void {
    console.log('=== Database Singleton Demo ===');

    // First instance
    const db1 = DatabaseConnection.getInstance('mongodb://localhost:27017/myapp');
    db1.connect();

    // Second instance - should be the same as the first one
    const db2 = DatabaseConnection.getInstance('postgres://localhost:5432/myapp');

    // Test if they are the same instance
    console.log('Are db1 and db2 the same instance?', db1 === db2);

    // The second connection string is ignored since the instance is already created
    console.log('Execute a query');
    try {
        const results = db1.executeQuery('SELECT * FROM users');
        console.log('Query results:', results);
    } catch (error) {
        console.error('Query error:', error.message);
    }

    db1.disconnect();
}

demonstrateDatabaseSingleton();
