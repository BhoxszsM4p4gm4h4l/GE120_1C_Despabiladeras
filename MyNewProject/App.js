import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import { dmsToDecimal, decimalToDms } from './path/to/converter'; // Update the path to where your converter functions are located

const TimeConverter = () => {
    const [dmsInput, setDmsInput] = useState('');
    const [decimalOutput, setDecimalOutput] = useState('');

    const convertDmsToDecimal = () => {
        const { minutes, seconds, milliseconds } = dmsInput.split(',').map(Number);
        const decimalTime = dmsToDecimal(minutes, seconds, milliseconds);
        setDecimalOutput(decimalTime.toString());
    };

    const convertDecimalToDms = () => {
        const { minutes, seconds, milliseconds } = decimalToDms(decimalInput).milliseconds? decimalToDms(decimalInput) : { minutes: 0, seconds: 0, milliseconds: 0 };
        setDmsOutput(dmsInput);
    };

    return (
        <View>
            <TextInput
                placeholder="Enter DMS (e.g., 1,30,500)"
                value={dmsInput}
                onChangeText={setDmsInput}
            />
            <Button title="Convert to Decimal" onPress={convertDmsToDecimal} />
            <Text>{decimalOutput}</Text>

            <TextInput
                placeholder="Enter Decimal"
                value={decimalInput}
                onChangeText={setDecimalInput} // Make sure to manage state for decimalInput
            />
            <Button title="Convert to DMS" onPress={convertDecimalToDms} />
            <Text>{dmsOutput}</Text> {/* Display converted DMS */}
        </View>
    );
};

export default TimeConverter;