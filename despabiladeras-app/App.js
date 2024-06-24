import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View } from 'react-native';

export default function App() {

  var name = 'dom'

  return (
    <View style={styles.container}>
      <Text>mariole was here
      </Text> 
      <View style={styles.box}> 
      </View>
      <TextInput
        style={styles.text} 
          onChangeText
      />
      <StatusBar style="auto" />
    </View>
   
  );
}
const styles = s 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'pink',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box: {
    backgroundColor: 'blue',
    height:'50%',
    width:'50%',
  },
});
