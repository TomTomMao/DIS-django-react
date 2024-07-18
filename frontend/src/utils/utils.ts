export default function replaceEmptyString(originalValue: string, valueToReplace: string): string {
    return originalValue === '' ? valueToReplace : originalValue
}