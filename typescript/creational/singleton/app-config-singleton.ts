/**
 * Singleton with State
 *
 * This implementation demonstrates a singleton that manages state
 * throughout the application.
 */
class ApplicationConfig {
    private static instance: ApplicationConfig;
    private settings: Map<string, any> = new Map();

    // Private constructor
    private constructor() {
        // Set default configuration
        this.settings.set('theme', 'light');
        this.settings.set('language', 'en');
        this.settings.set('notifications', true);
        console.log('Application configuration initialized with default settings');
    }

    // Get singleton instance
    public static getInstance(): ApplicationConfig {
        if (!ApplicationConfig.instance) {
            ApplicationConfig.instance = new ApplicationConfig();
        }
        return ApplicationConfig.instance;
    }

    // Get a configuration value
    public get(key: string): any {
        if (!this.settings.has(key)) {
            throw new Error(`Configuration key "${key}" does not exist`);
        }
        return this.settings.get(key);
    }

    // Set a configuration value
    public set(key: string, value: any): void {
        this.settings.set(key, value);
        console.log(`Configuration updated: ${key} = ${value}`);
    }

    // Check if a configuration exists
    public has(key: string): boolean {
        return this.settings.has(key);
    }

    // Reset to defaults
    public resetToDefaults(): void {
        this.settings.clear();
        this.settings.set('theme', 'light');
        this.settings.set('language', 'en');
        this.settings.set('notifications', true);
        console.log('Configuration reset to defaults');
    }

    // Get all configuration as an object
    public getAllSettings(): Record<string, any> {
        const settingsObject: Record<string, any> = {};
        this.settings.forEach((value, key) => {
            settingsObject[key] = value;
        });
        return settingsObject;
    }
}

function demonstrateConfigSingleton(): void {
    console.log('\n=== Application Config Singleton Demo ===');

    // Get config instance
    const config1 = ApplicationConfig.getInstance();

    // Display default configuration
    console.log('Default configuration:', config1.getAllSettings());

    // Update some settings
    config1.set('theme', 'dark');
    config1.set('fontSize', 14);

    // Get another reference to the same instance
    const config2 = ApplicationConfig.getInstance();

    // Show that changes are visible through both references
    console.log('Updated configuration via config2:', config2.getAllSettings());

    // Make more changes through the second reference
    config2.set('language', 'fr');

    // Show changes are reflected in the first reference
    console.log('Theme setting via config1:', config1.get('theme'));
    console.log('Language setting via config1:', config1.get('language'));

    // Reset to defaults
    config1.resetToDefaults();
    console.log('After reset via config1, config2 shows:', config2.getAllSettings());
}

demonstrateConfigSingleton();
