/**
 * A class for containing a group of many different kinds of die.
 */
class DiceSet {
    public diceGroups: Array<DiceGroup>;

    /**
     * The constructor can take in an array of DiceGroup objects, however
     *  a default constructor can be used which will set up some classic
     *  DiceGroup configurations.
     */
    public constructor();
    public constructor(diceGroups: Array<DiceGroup>);
    public constructor(diceGroups?: Array<DiceGroup>) {
        this.diceGroups = diceGroups ?? [
            new DiceGroup(4, [new Die(4)]),
            new DiceGroup(6, [new Die(6)]),
            new DiceGroup(8, [new Die(8)]),
            new DiceGroup(10, [new Die(10)]),
            new DiceGroup(12, [new Die(12)]),
            new DiceGroup(20, [new Die(20)]),
        ];
    }

    /**
     * Adds a new DiceGroup to the DiceSet, provided an equivalent does
     *  not already exist.
     */
    public addGroup(inGroup: DiceGroup): void {
        this.diceGroups.forEach( (element) => {
            if (element.diceType === inGroup.diceType) {
                return(null); // Terminate early because DiceGroup was found
            }
        });

        this.diceGroups.push(inGroup); // Add unique DiceGroup to DiceSet
    }

    /**
     * Rolls every Die inside every DiceGroup and outputs the total as well
     *  as the result of each individual Die.
     */
    public rollSet(): [number, Array<number>] {
        let total: number = 0;
        let rolls: Array<number> = [];

        this.diceGroups.forEach( (element) => {
            total += element.rollGroup()[0];
            rolls.push(element.rollGroup()[1][0]); // only prints 1st in Group
        });
        
        return([total, rolls]);
    }
}
