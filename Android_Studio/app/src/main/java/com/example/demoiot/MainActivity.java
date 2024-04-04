package com.example.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class MainActivity extends AppCompatActivity {
    MQTTHelper mqttHelper;
    TextView txtTemperature, txtHumidity, txtLight, txtAI;
    LabeledSwitch btnLED, btnAC;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtTemperature = findViewById(R.id.txtTemperature);
        txtHumidity = findViewById(R.id.txtHumidity);
        txtLight = findViewById(R.id.txtLight);
        txtAI= findViewById(R.id.txtAI);
        btnLED = findViewById(R.id.nutnhan1);
        btnAC = findViewById(R.id.nutnhan2);

        btnLED.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn == true){
                    sendDataMQTT("CE_LHuy/feeds/nutnhan1", "1");
                } else{
                    sendDataMQTT("CE_LHuy/feeds/nutnhan1", "0");
                }
            }
        });
        btnAC.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn == true){
                    sendDataMQTT("CE_LHuy/feeds/nutnhan2", "1");
                } else{
                    sendDataMQTT("CE_LHuy/feeds/nutnhan2", "0");
                }
            }
        });
        startMQTT();
    }

    public void sendDataMQTT(String topic, String value){
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }
    }

    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + "***" + message.toString());
                if(topic.contains("sensor1")){
                    txtTemperature.setText(message.toString() + "°C");
                } else if (topic.contains("sensor2")){
                    txtTemperature.setText(message.toString() + "%");
                } else if(topic.contains("sensor3")) {
                    txtTemperature.setText(message.toString() + "%");
                } else if(topic.contains("nutnhan1")){
                    if(message.toString().equals("1")){
                        btnLED.setOn(true);
                    }else{
                        btnLED.setOn(false);
                    }
                } else if(topic.contains("nutnhan2")){
                    if(message.toString().equals("1")){
                        btnAC.setOn(true);
                    }else{
                        btnAC.setOn(false);
                    }
                }

            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}