import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "material-ui/styles";
import Table, { TableBody, TableCell, TableRow } from "material-ui/Table";

const styles = theme => ({});

let id = 0;
function createData(name, calories, fat, carbs, protein) {
  id += 1;
  return { id, name, calories, fat, carbs, protein };
}

const data = [
  createData("Source MAC", 159, 6.0, 24, 4.0),
  createData("Source IP", 237, 9.0, 37, 4.3),
  createData("Source Port", 262, 16.0, 24, 6.0),
  createData("Dest MAC", 237, 9.0, 37, 4.3),
  createData("Dest IP", 237, 9.0, 37, 4.3),
  createData("Dest Port", 237, 9.0, 37, 4.3),
  createData("Protocol", 237, 9.0, 37, 4.3),
  createData("Good packet", 237, 9.0, 37, 4.3),
  createData("Allowed", 237, 9.0, 37, 4.3)
];

function SimpleTable(props) {
  return (
    <Table>
      <TableBody>
        {data.map(n => {
          return (
            <TableRow key={n.id}>
              <TableCell>{n.name}</TableCell>
              <TableCell numeric>{n.calories}</TableCell>
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
}

SimpleTable.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SimpleTable);
