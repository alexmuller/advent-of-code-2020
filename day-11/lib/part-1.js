const getAdjacentSeatIds = ((seatId, lineLength, numSeats) => {
    if (seatId >= numSeats) {
        throw `Seat ID ${seatId} too high`;
    }

    let potentialSeats = [];

    let leftColumn = seatId % lineLength === 0;
    let rightColumn = seatId % lineLength === lineLength - 1;

    if (leftColumn) {
        potentialSeats.push(
            seatId-lineLength, seatId-lineLength+1,
            seatId+1,
            seatId+lineLength, seatId+lineLength+1,
        )
    } else if (rightColumn) {
        potentialSeats.push(
            seatId-lineLength-1, seatId-lineLength,
            seatId-1,
            seatId+lineLength-1, seatId+lineLength,
        )
    } else {
        potentialSeats.push(
            seatId-lineLength-1, seatId-lineLength, seatId-lineLength+1,
            seatId-1, seatId+1,
            seatId+lineLength-1, seatId+lineLength, seatId+lineLength+1,
        );
    }

    return potentialSeats.filter(seat => 0 <= seat && seat < numSeats);
})

const part1 = ((contents) => {
    const lineLength = contents.split('\n')[0].length;
    let seatingPlan = contents.replace(/\n/g, '');
    const numSeats = seatingPlan.length;

    while (true) {
        let nextSeatingPlan = '';

        [...seatingPlan].forEach((c, i) => {
            let seatsToInspect = getAdjacentSeatIds(i, lineLength, numSeats)
            let adjacentSeats = seatsToInspect.map(i => seatingPlan.charAt(i))
            let numberOfOccupied = adjacentSeats.filter(seat => seat === '#').length;
            if (c === '.') {
                nextSeatingPlan += '.';
            } else if (c === 'L') {
                if (adjacentSeats.includes('#')) {
                    nextSeatingPlan += 'L';
                } else {
                    nextSeatingPlan += '#';
                }
            } else if (c === '#') {
                if (numberOfOccupied >= 4) {
                    nextSeatingPlan += 'L';
                } else {
                    nextSeatingPlan += '#';
                }
            } else {
                nextSeatingPlan += '?';
            }
        });

        if (nextSeatingPlan === seatingPlan) {
            return nextSeatingPlan.split('').filter(seat => seat === '#').length;
        } else {
            seatingPlan = nextSeatingPlan;
        }

    }
});

module.exports = part1;
