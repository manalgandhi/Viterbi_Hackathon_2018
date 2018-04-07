import React, { Component } from "react";
import axios from "axios";
import CssBaseline from "material-ui/CssBaseline";
import Grid from "material-ui/Grid";
import Button from "material-ui/Button";
import { withStyles } from "material-ui/styles";
import SimpleExtentionPanels from "./SimpleExtentionPanels";
import SimpleNestedList from "./SimpleNestedList";

const styles = theme => ({
  app: {
    margin: "3%"
  }
});

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      devices: [
        {
          name: "namename",
          packets: [{ srcIp: "srcIpsrcIp" }]
        }
      ],
      chosenDeviceIdx: -1
    };
    this.fetchDevices = this.fetchDevices.bind(this);
    this.handleDeviceClicked = this.handleDeviceClicked.bind(this);
  }

  handleDeviceClicked(idx) {
    this.setState({ chosenDeviceIdx: idx });
    console.log("eee");
  }

  fetchDevices() {
    const that = this;
    axios({
      method: "get",
      url: "http://127.0.0.1:8080/devices",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(function(response) {
        that.setState({ devices: response.data.devices });
      })
      .catch(function(error) {
        console.log(error);
      });
  }

  render() {
    const { classes } = this.props;
    const devicesPackets = [
      { name: "14:21 04-07 2018", values: ["aaa", "bbbb"] },
      { name: "14:35 04-07 2018", values: ["aaa", "bbbb"] }
    ];
    return (
      <React.Fragment>
        <CssBaseline />
        <div className={classes.app}>
          <header className="App-header">
            <h1 className="App-title">TEAM 1</h1>
          </header>
          <Grid container spacing={16}>
            <Grid item xs={6}>
              <Button
                onClick={this.fetchDevices}
                variant="raised"
                color="primary"
              >
                Fetch devices
              </Button>
              <h2>Devices we detected</h2>
              <SimpleNestedList
                devices={this.state.devices}
                chosenDeviceIdx={this.state.chosenDeviceIdx}
                handleDeviceClicked={this.handleDeviceClicked}
              />
            </Grid>
            <Grid item xs={6}>
              <h2>Packets the device sent/received</h2>
              <SimpleExtentionPanels devicesPackets={devicesPackets} />
            </Grid>
          </Grid>
        </div>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(App);
