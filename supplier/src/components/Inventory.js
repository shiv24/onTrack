import React, { Component } from 'react'
import { Button } from 'react-bootstrap'

export default class Inventory extends Component {
	render() {
		const { id, productCode, name, price, category, onEdit, onDelete } = this.props
		return (
			<tr>
				<td>{productCode}</td>
		        <td>{name}</td>
		        <td>{price}</td>
		        <td>{category}</td>
		        <td><Button bsStyle="info" onClick={() => onEdit(id) }>Edit</Button></td>
		        <td><Button bsStyle="danger" onClick={() => onDelete(id) }>Delete</Button></td>
		    </tr>
		);
	}
}
